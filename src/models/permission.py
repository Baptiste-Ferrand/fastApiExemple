from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.models import Base

class Permission(Base):
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    roles = relationship("Role", secondary="role_permissions", back_populates="permissions")
