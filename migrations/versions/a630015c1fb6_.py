"""empty message

Revision ID: a630015c1fb6
Revises: 0df1fec75e55
Create Date: 2025-01-02 08:54:01.840303

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a630015c1fb6'
down_revision = '0df1fec75e55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('course', sa.String(length=100), nullable=False),
    sa.Column('mentor', sa.String(length=30), nullable=False),
    sa.Column('title', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('course_id'),
    sa.UniqueConstraint('course')
    )
    op.create_table('user_course',
    sa.Column('userCourse_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.course_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('userCourse_id')
    )
    op.drop_table('usercourse')
    with op.batch_alter_table('corses', schema=None) as batch_op:
        batch_op.drop_index('course')

    op.drop_table('corses')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('corses',
    sa.Column('course_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('course', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('mentor', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('title', mysql.VARCHAR(length=30), nullable=False),
    sa.PrimaryKeyConstraint('course_id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('corses', schema=None) as batch_op:
        batch_op.create_index('course', ['course'], unique=True)

    op.create_table('usercourse',
    sa.Column('userCourse_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('course_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['corses.course_id'], name='usercourse_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], name='usercourse_ibfk_2'),
    sa.PrimaryKeyConstraint('userCourse_id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('user_course')
    op.drop_table('courses')
    # ### end Alembic commands ###