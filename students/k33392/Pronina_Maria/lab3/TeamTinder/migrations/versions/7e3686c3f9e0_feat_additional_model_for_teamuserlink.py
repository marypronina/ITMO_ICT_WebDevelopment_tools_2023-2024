"""feat: additional model for TeamUserLink

Revision ID: 7e3686c3f9e0
Revises: 1ed21834a5c7
Create Date: 2024-06-01 15:09:53.858852

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '7e3686c3f9e0'
down_revision: Union[str, None] = '1ed21834a5c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
