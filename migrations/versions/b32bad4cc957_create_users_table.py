"""create users table

Revision ID: b32bad4cc957
Revises: 
Create Date: 2023-06-28 02:00:48.072262

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b32bad4cc957'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('firstname', sa.String(), nullable=False),
                    sa.Column('lastname', sa.String(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('gender', sa.Enum('female', 'male', name='gender'), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###