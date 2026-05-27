"""merge remaining head

Revision ID: 24cd912d36f2
Revises: 518387e7187a
Create Date: 2026-05-18 19:05:59.074464

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '24cd912d36f2'
down_revision: Union[str, None] = '518387e7187a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
