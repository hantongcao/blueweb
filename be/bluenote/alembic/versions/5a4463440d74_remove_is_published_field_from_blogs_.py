"""Remove is_published field from blogs table

Revision ID: 5a4463440d74
Revises: cd222181b027
Create Date: 2025-07-16 14:21:27.957308

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a4463440d74'
down_revision: Union[str, None] = 'cd222181b027'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'is_published')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('is_published', sa.BOOLEAN(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
