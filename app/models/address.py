from __future__ import annotations
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base


class Address(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    addressline1: Mapped[str] = mapped_column(String(256))
    addressline2: Mapped[str] = mapped_column(String(256))
    city: Mapped[str] = mapped_column(String(128))
    state: Mapped[str] = mapped_column(String(128))
    postalcode: Mapped[str] = mapped_column(String(56))
    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("accounts.id"))
    contact_id: Mapped[int] = mapped_column(Integer, ForeignKey("contacts.id"))
