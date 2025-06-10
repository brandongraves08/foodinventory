"""Initial migration

Revision ID: 001
Revises: 
Create Date: 2025-06-10

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create food_item table
    op.create_table(
        'fooditem',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('name', sa.String(), nullable=False, index=True),
        sa.Column('barcode', sa.String(), nullable=True, index=True),
        sa.Column('category', sa.String(), nullable=True, index=True),
        sa.Column('quantity', sa.Integer(), nullable=False, default=1),
        sa.Column('expiration_date', sa.Date(), nullable=True),
        sa.Column('image_url', sa.String(), nullable=True),
        sa.Column('source', sa.String(), nullable=False),
        sa.Column('added_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table('fooditem')