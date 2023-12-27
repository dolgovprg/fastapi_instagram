"""Updated user model: added username field

Revision ID: 5935858e17bc
Revises: 1e6869d821d7
Create Date: 2022-06-09 16:49:07.178831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5935858e17bc'
down_revision = '1e6869d821d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=25), nullable=False))
    op.create_unique_constraint('username_constraint', 'user', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('username_constraint', 'user', type_='unique')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###
