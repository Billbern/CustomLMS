from __future__ import annotations
from typing import List
from sqlalchemy import Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base
from app.models.course import Course
from app.models.category import Category


class Program(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    categories: Mapped[List[Category]] = relationship(
        "Category", back_populates="programcategories"
    )
    courses: Mapped[List[Course]] = relationship(
        "Course", back_populates="programcourses"
    )
