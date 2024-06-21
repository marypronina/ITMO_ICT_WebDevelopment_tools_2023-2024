"""foreign keys fixes

Revision ID: cf516e96fa15
Revises: ec25d08aebe9
Create Date: 2024-06-01 13:38:04.462645

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'cf516e96fa15'
down_revision: Union[str, None] = 'ec25d08aebe9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('userproject_team_project_id_fkey', 'userproject', type_='foreignkey')
    op.drop_column('userproject', 'team_project_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('userproject', sa.Column('team_project_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('userproject_team_project_id_fkey', 'userproject', 'teamproject', ['team_project_id'], ['id'])
    # ### end Alembic commands ###
