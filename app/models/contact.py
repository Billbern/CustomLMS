from __future__ import annotations
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base


class Contact(Base):
    id: Mapped[id] = mapped_column(Integer, primary_key=True, index=True)
    phone1: Mapped[str] = mapped_column(String(20))
    phone2: Mapped[str] = mapped_column(String(20))
    phone3: Mapped[str] = mapped_column(String(20))
    address_id: Mapped[int] = mapped_column(Integer, ForeignKey("addresses.id"))
    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("accounts.id"))
