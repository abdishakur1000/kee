"""add content column to posts table

Revision ID: 9a27282db768
Revises: 9596efad3fba
Create Date: 2022-06-29 08:12:56.582084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a27282db768'
down_revision = '9596efad3fba'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
