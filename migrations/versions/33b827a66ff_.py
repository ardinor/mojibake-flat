"""empty message

Revision ID: 33b827a66ff
Revises: None
Create Date: 2013-10-10 15:30:43.628000

"""

# revision identifiers, used by Alembic.
revision = '33b827a66ff'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.Column('path', sa.String(length=240), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('categories', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    ### end Alembic commands ###