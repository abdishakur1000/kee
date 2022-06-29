"""add last few columns to posts table

Revision ID: 9a447407e16e
Revises: 87e1cc7b1bf3
Create Date: 2022-06-29 10:26:36.205561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a447407e16e'
down_revision = '87e1cc7b1bf3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),
                  op.add_column('posts', sa.Column(
                      'created_at', sa.TIMESTAMP(timezone=True), nullable=False,
                      server_default=sa.text('NOW()')),))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
