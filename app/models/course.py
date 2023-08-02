from __future__ import annotations
from typing import List
from sqlalchemy import Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base
from app.models.category import Category
from app.models.content import Content


class Course(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(256), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    categories: Mapped[List[Category]] = relationship(
        "Category", back_populates="coursecategories"
    )
    contents: Mapped[List[Content]] = relationship(
        "Content", back_populates="coursecontent"
    )
