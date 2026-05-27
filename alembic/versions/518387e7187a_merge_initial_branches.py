"""merge initial branches

Revision ID: 518387e7187a
Revises: 2d42c5cf68dd
Create Date: 2026-05-18 19:05:00.197991

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '518387e7187a'
down_revision: Union[str, None] = '2d42c5cf68dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
