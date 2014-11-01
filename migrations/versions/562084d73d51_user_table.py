"""user table

Revision ID: 562084d73d51
Revises: None
Create Date: 2014-11-01 13:10:19.473239

"""

# revision identifiers, used by Alembic.
revision = '562084d73d51'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(u'ix_users_email', 'users', ['email'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(u'ix_users_email', table_name='users')
    op.drop_table('users')
    ### end Alembic commands ###
