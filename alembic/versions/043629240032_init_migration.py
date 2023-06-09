"""Init migration

Revision ID: 043629240032
Revises: 
Create Date: 2023-04-22 19:32:06.856619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '043629240032'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('banned', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
