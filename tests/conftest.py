import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from dependencies import pegar_sessao
from main import app
from models import Base, Usuario
from security import bcrypt_context


TEST_DATABASE_URL = "sqlite://"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


@pytest.fixture()
def db_session():
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()

    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def client(db_session):
    def override_pegar_sessao():
        yield db_session

    app.dependency_overrides[pegar_sessao] = override_pegar_sessao

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


@pytest.fixture()
def test_user(db_session):
    usuario = Usuario(
        nome="Test User",
        email="test@example.com",
        senha=bcrypt_context.hash("test123"),
        ativo=True,
        admin=False,
    )

    db_session.add(usuario)
    db_session.commit()
    db_session.refresh(usuario)

    return usuario
