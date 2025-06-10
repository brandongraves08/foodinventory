"""Add owner relationship to food items

Revision ID: 003
Revises: 002
Create Date: 2025-06-10

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '003'
down_revision = '002'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add owner_id column to fooditem table
    op.add_column('fooditem', sa.Column('owner_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key(
        "fk_fooditem_owner_id",
        "fooditem",
        "user",
        ["owner_id"],
        ["id"],
    )


def downgrade() -> None:
    op.drop_constraint("fk_fooditem_owner_id", "fooditem", type_="foreignkey")
    op.drop_column('fooditem', 'owner_id')