"""add category

Revision ID: 4852b802b6d8
Revises: 6f666a2ed342
Create Date: 2018-02-05 17:59:10.397271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4852b802b6d8'
down_revision = '6f666a2ed342'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id', name='category_pkey')
    )
    op.drop_table('categories')
    # ### end Alembic commands ###