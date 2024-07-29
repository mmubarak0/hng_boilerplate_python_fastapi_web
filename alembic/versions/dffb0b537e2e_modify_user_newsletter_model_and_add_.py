"""Modify User, Newsletter model and Add NewsletterSubscriber models

Revision ID: dffb0b537e2e
# Revises: e30fc0cc2d35
Create Date: 2024-07-28 20:30:18.369953

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect


# revision identifiers, used by Alembic.
revision: str = 'dffb0b537e2e'
down_revision: Union[str, None] = 'e30fc0cc2d35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    if inspect(op.get_bind()).has_table('user_newsletter_association'):
        op.execute('DROP TABLE user_newsletter_association CASCADE')

    if inspect(op.get_bind()).has_table('newsletters'):
        op.drop_table('newsletters')


    op.create_table('newsletters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('newsletter_subscribers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('newsletter_id', sa.Integer(), nullable=True),
    sa.Column('subscribed_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['newsletter_id'], ['newsletters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_organization', 'status')
    op.drop_table('newsletter_subscribers')
    op.drop_table('newsletters')
    # ### end Alembic commands ###
