"""initial migration

Revision ID: 9848ad5ec3f6
Revises: 00806fcbb0da
Create Date: 2017-12-28 14:20:38.735121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9848ad5ec3f6'
down_revision = '00806fcbb0da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###