from __future__ import annotations
from typing import List
from sqlalchemy import Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base
from app.models.address import Address
from app.models.permission import Permission


class Account(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    firstname: Mapped[str] = mapped_column(String(256), nullable=False)
    middlename: Mapped[str] = mapped_column(String(256), nullable=True)
    lastname: Mapped[str] = mapped_column(String(256), nullable=False)
    email: Mapped[str] = mapped_column(
        String(128), index=True, nullable=False, unique=True
    )
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    user_type: Mapped[Enum] = mapped_column(
        Enum("student", "tutor", "admin"), default="student"
    )
    addresses: Mapped[List(Address)] = relationship(
        "Address", back_populates="addresses"
    )
    permissions: Mapped[List(Permission)] = relationship(
        "Permission", back_populates="accountpermissions"
    )
