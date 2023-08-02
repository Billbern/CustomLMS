from __future__ import annotations
from typing import List
from sqlalchemy import Integer, String, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base
from app.models.address import Address


class Varsity(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    website: Mapped[str] = mapped_column(String(128), nullable=True)
    addresses: Mapped[List[Address]] = relationship(
        "Address", back_populates="varsityaddresses"
    )
