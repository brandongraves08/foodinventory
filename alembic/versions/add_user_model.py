"""Add user model

Revision ID: 002
Revises: 001
Create Date: 2025-06-10

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '002'
down_revision = '001'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create user table
    op.create_table(
        'user',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('email', sa.String(), nullable=False, index=True, unique=True),
        sa.Column('username', sa.String(), nullable=False, index=True, unique=True),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, default=True),
        sa.Column('is_superuser', sa.Boolean(), nullable=False, default=False),
    )


def downgrade() -> None:
    op.drop_table('user')