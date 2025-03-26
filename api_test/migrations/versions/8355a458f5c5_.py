"""empty message

Revision ID: 8355a458f5c5
Revises: d9e6a887797d
Create Date: 2025-03-26 18:37:58.940794

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '8355a458f5c5'
down_revision: Union[str, None] = 'd9e6a887797d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_nav_id', table_name='nav')
    op.drop_table('nav')
    op.drop_index('ix_rebalance_id', table_name='rebalance')
    op.drop_table('rebalance')
    op.add_column('backtest_requests', sa.Column('nav_result', postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    op.add_column('backtest_requests', sa.Column('rebalance_result', postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    op.drop_constraint('uq_prices_date_ticker', 'prices', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uq_prices_date_ticker', 'prices', ['date', 'ticker'])
    op.drop_column('backtest_requests', 'rebalance_result')
    op.drop_column('backtest_requests', 'nav_result')
    op.create_table('rebalance',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('data_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('ticker', sa.VARCHAR(length=10), autoincrement=False, nullable=False),
    sa.Column('weight', sa.NUMERIC(precision=3, scale=2), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['data_id'], ['backtest_requests.data_id'], name='rebalance_data_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='rebalance_pkey')
    )
    op.create_index('ix_rebalance_id', 'rebalance', ['id'], unique=False)
    op.create_table('nav',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('data_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('nav_total', sa.NUMERIC(precision=15, scale=2), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['data_id'], ['backtest_requests.data_id'], name='nav_data_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='nav_pkey')
    )
    op.create_index('ix_nav_id', 'nav', ['id'], unique=False)
    # ### end Alembic commands ###
