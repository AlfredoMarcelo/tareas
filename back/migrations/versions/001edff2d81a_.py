"""empty message

Revision ID: 001edff2d81a
Revises: 
Create Date: 2021-12-22 16:39:25.005944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001edff2d81a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tareas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tarea', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tareas')
    # ### end Alembic commands ###