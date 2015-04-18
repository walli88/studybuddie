"""empty message

Revision ID: 27e9685a4d41
Revises: 251f3cafad7d
Create Date: 2015-04-18 11:15:14.182902

"""

# revision identifiers, used by Alembic.
revision = '27e9685a4d41'
down_revision = '251f3cafad7d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('signup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_signup_email'), 'signup', ['email'], unique=True)
    op.create_table('tutor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('fullname', sa.String(length=64), nullable=True),
    sa.Column('school', sa.String(length=64), nullable=True),
    sa.Column('grade', sa.String(length=64), nullable=True),
    sa.Column('major', sa.String(length=64), nullable=True),
    sa.Column('gpa', sa.Float(), nullable=True),
    sa.Column('phonenumber', sa.String(length=10), nullable=True),
    sa.Column('relexp', sa.String(length=500), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('fullname', sa.String(length=64), nullable=True),
    sa.Column('school', sa.String(length=64), nullable=True),
    sa.Column('grade', sa.String(length=64), nullable=True),
    sa.Column('phonenumber', sa.String(length=10), nullable=True),
    sa.Column('major', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('get_help',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('class_number', sa.String(length=64), nullable=True),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.Column('help_comment', sa.String(length=64), nullable=True),
    sa.Column('duration', sa.String(length=64), nullable=True),
    sa.Column('start_datetime', sa.DateTime(), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('get_help')
    op.drop_table('student')
    op.drop_table('tutor')
    op.drop_index(op.f('ix_signup_email'), table_name='signup')
    op.drop_table('signup')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    ### end Alembic commands ###
