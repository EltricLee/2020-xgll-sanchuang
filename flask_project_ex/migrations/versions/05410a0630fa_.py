"""empty message

Revision ID: 05410a0630fa
Revises: 
Create Date: 2020-07-15 11:26:58.321187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05410a0630fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.add_column(sa.Column('count2', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.drop_column('count2')

    # ### end Alembic commands ###