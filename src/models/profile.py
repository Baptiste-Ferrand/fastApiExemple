from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from src.models import Base

class Profile(Base):
    __tablename__ = "profiles"
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    firstname = Column(String, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.uuid", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="profile")
