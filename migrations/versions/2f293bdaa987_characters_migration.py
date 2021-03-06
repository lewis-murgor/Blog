"""characters migration

Revision ID: 2f293bdaa987
Revises: d1168fc41a41
Create Date: 2022-03-14 08:48:17.948248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f293bdaa987'
down_revision = 'd1168fc41a41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('text', sa.String(length=700), nullable=True))
    op.add_column('comments', sa.Column('comment', sa.String(length=700), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'comment')
    op.drop_column('blogs', 'text')
    # ### end Alembic commands ###
