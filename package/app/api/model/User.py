from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from package.app import sqlalchemy_base
from package.app.api.model.Role import Role


class User(sqlalchemy_base):

    __tablename__ = "tb_user"

    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    role_id = Column(Integer, ForeignKey("tb_role.id"))

    role = relationship(Role)
