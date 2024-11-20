from sqlalchemy import Table, Column, Integer, ForeignKey
from src.models import Base
from sqlalchemy.dialects.postgresql import UUID

user_roles = Table(
    'user_roles',
    Base.metadata,
    Column('user_id', UUID(as_uuid=True), ForeignKey('users.uuid', ondelete="CASCADE"), primary_key=True),
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True)
)