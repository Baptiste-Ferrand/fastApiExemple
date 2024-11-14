from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.models import Base


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    permissions = relationship("Permission", secondary="role_permissions", back_populates="roles")
