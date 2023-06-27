from alembic import op
import sqlalchemy as sa

revision = "3ac89b60e26f"
down_revision = "2230ba041691"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("firstname", sa.String(), nullable=False),
        sa.Column("lastname", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column(
            "gender", sa.Enum("female", "male", name="gender_type"), nullable=True
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("users")
