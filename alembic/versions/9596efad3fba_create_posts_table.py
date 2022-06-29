"""create posts table

Revision ID: 9596efad3fba
Revises: d7f161ffe1e8
Create Date: 2022-06-29 08:06:04.514452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9596efad3fba'
down_revision = 'd7f161ffe1e8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                                       primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
