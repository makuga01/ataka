from sqlalchemy import Column, Integer, String

from ..config import Base, JsonBase


class Target(Base, JsonBase):
    __tablename__ = "targets"

    id = Column(Integer, primary_key=True)
    ip = Column(String)
    service_id = Column(String)
    service_name = Column(String)