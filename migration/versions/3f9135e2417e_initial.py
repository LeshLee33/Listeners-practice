"""initial

Revision ID: 3f9135e2417e
Revises: 
Create Date: 2025-03-04 23:35:26.703458

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f9135e2417e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course',
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('course_title', sa.String(), nullable=False),
    sa.Column('duration_hours', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('course_id')
    )
    op.create_index(op.f('ix_course_course_id'), 'course', ['course_id'], unique=False)
    op.create_table('listener',
    sa.Column('listener_id', sa.Integer(), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.Column('sex', sa.String(), nullable=False),
    sa.Column('citizenship', sa.String(), nullable=False),
    sa.Column('country', sa.String(), nullable=False),
    sa.Column('region', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('listener_id')
    )
    op.create_index(op.f('ix_listener_listener_id'), 'listener', ['listener_id'], unique=False)
    op.create_table('assignment',
    sa.Column('assignment_id', sa.Integer(), nullable=False),
    sa.Column('listener_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('education', sa.String(), nullable=False),
    sa.Column('education_institution', sa.String(), nullable=False),
    sa.Column('discipline', sa.String(), nullable=False),
    sa.Column('qualification', sa.String(), nullable=False),
    sa.Column('listener_category_one', sa.String(), nullable=False),
    sa.Column('listener_category_two', sa.String(), nullable=True),
    sa.Column('listener_category_three', sa.String(), nullable=True),
    sa.Column('tusur_student', sa.Boolean(), nullable=False),
    sa.Column('post', sa.String(), nullable=True),
    sa.Column('job', sa.String(), nullable=True),
    sa.Column('assignment_status', sa.String(), nullable=False),
    sa.Column('department', sa.String(), nullable=True),
    sa.Column('education_format', sa.String(), nullable=False),
    sa.Column('education_form', sa.String(), nullable=True),
    sa.Column('assignment_date', sa.Date(), nullable=False),
    sa.Column('is_an_organization', sa.Boolean(), nullable=False),
    sa.Column('organization_name', sa.String(), nullable=True),
    sa.Column('study_start', sa.Date(), nullable=False),
    sa.Column('study_end', sa.Date(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('paid', sa.Integer(), nullable=False),
    sa.Column('expulsion_reason', sa.String(), nullable=True),
    sa.Column('where_had_known_about_course', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.course_id'], ),
    sa.ForeignKeyConstraint(['listener_id'], ['listener.listener_id'], ),
    sa.PrimaryKeyConstraint('assignment_id')
    )
    op.create_index(op.f('ix_assignment_assignment_id'), 'assignment', ['assignment_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_assignment_assignment_id'), table_name='assignment')
    op.drop_table('assignment')
    op.drop_index(op.f('ix_listener_listener_id'), table_name='listener')
    op.drop_table('listener')
    op.drop_index(op.f('ix_course_course_id'), table_name='course')
    op.drop_table('course')
    # ### end Alembic commands ###
