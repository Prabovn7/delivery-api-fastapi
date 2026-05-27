"""merge remaining to single head

Revision ID: d3c8957a010f
Revises: 24cd912d36f2
Create Date: 2026-05-18 19:06:09.148227

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd3c8957a010f'
down_revision: Union[str, None] = '24cd912d36f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
