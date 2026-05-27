"""final merge

Revision ID: 891ef36dca5e
Revises: 34fa7a6b23fd, d3c8957a010f
Create Date: 2026-05-18 19:06:19.237422

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '891ef36dca5e'
down_revision: Union[str, None] = ('34fa7a6b23fd', 'd3c8957a010f')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
