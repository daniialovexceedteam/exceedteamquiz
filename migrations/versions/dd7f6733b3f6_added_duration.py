"""added duration

Revision ID: dd7f6733b3f6
Revises: a3d5648c8fcf
Create Date: 2022-08-31 17:32:10.803378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd7f6733b3f6'
down_revision = 'a3d5648c8fcf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tests', sa.Column('duration', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tests', 'duration')
    # ### end Alembic commands ###
