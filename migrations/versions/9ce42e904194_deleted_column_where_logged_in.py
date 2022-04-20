"""Deleted column where_logged_in

Revision ID: 9ce42e904194
Revises: 740b4c9a16fd
Create Date: 2022-04-20 20:43:07.462520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ce42e904194'
down_revision = '740b4c9a16fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Login', schema=None) as batch_op:
        batch_op.drop_column('where_logged_in')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Login', schema=None) as batch_op:
        batch_op.add_column(sa.Column('where_logged_in', sa.VARCHAR(length=120), nullable=True))

    # ### end Alembic commands ###