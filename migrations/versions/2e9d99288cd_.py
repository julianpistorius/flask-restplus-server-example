"""empty message

Revision ID: 2e9d99288cd
Revises: 36954739c63
Create Date: 2015-11-23 21:16:54.103342

"""

# revision identifiers, used by Alembic.
revision = '2e9d99288cd'
down_revision = '36954739c63'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user') as batch_op:
        batch_op.alter_column('created',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('updated',
               existing_type=sa.DATETIME(),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user') as batch_op:
        batch_op.alter_column('updated',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('created',
               existing_type=sa.DATETIME(),
               nullable=True)
    ### end Alembic commands ###