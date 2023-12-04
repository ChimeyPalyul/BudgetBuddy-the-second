"""empty message

Revision ID: e1321292639c
Revises: 
Create Date: 2023-12-04 12:34:14.140354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1321292639c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories')
    op.drop_table('expenses')
    op.drop_table('incomes')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('username', sa.VARCHAR(), nullable=True),
    sa.Column('_password_hash', sa.VARCHAR(), nullable=True),
    sa.Column('income_id', sa.INTEGER(), nullable=False),
    sa.Column('expense_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['expense_id'], ['expenses.id'], name='fk_users_expense_id_expenses'),
    sa.ForeignKeyConstraint(['income_id'], ['incomes.id'], name='fk_users_income_id_incomes'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('incomes',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('amount', sa.FLOAT(), nullable=True),
    sa.Column('date', sa.DATETIME(), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('expenses',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('amount', sa.FLOAT(), nullable=True),
    sa.Column('date', sa.DATETIME(), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categories',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('parent_id', sa.INTEGER(), nullable=True),
    sa.Column('income_id', sa.INTEGER(), nullable=False),
    sa.Column('expense_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['expense_id'], ['expenses.id'], name='fk_categories_expense_id_expenses'),
    sa.ForeignKeyConstraint(['income_id'], ['incomes.id'], name='fk_categories_income_id_incomes'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###