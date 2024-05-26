"""empty message

Revision ID: aa37a7b915b2
Revises: 9d5b344c1ff0
Create Date: 2024-05-22 21:24:08.593276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa37a7b915b2'
down_revision = '9d5b344c1ff0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('pet_friendly', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('breed', sa.String(length=50), nullable=False),
    sa.Column('sex', sa.String(length=10), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('pedigree', sa.Boolean(), nullable=False),
    sa.Column('photo', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pets')
    op.drop_table('city')
    # ### end Alembic commands ###
