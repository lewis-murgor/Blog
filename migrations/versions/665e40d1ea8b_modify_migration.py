"""modify migration

Revision ID: 665e40d1ea8b
Revises: d5c525036ebf
Create Date: 2022-03-14 17:17:08.116427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '665e40d1ea8b'
down_revision = 'd5c525036ebf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'text')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('text', sa.VARCHAR(length=700), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
