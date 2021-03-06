"""followers

Revision ID: d027c14eb635
Revises: 2a9652b7481b
Create Date: 2019-05-16 19:22:05.032012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d027c14eb635"
down_revision = "2a9652b7481b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "followers",
        sa.Column("follower_id", sa.Integer(), nullable=True),
        sa.Column("followed_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["followed_id"], ["user.id"]),
        sa.ForeignKeyConstraint(["follower_id"], ["user.id"]),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("followers")
    # ### end Alembic commands ###
