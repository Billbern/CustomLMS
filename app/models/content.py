from __future__ import annotations
from typing import List
from sqlalchemy import Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base


class Content(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(256), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    course_id: Mapped[int] = mapped_column(Integer, ForeignKey("courses.id"))
    parent_content_id: Mapped[int] = mapped_column(Integer, ForeignKey("contents.id"))
    sub_content: Mapped[List[Content]] = relationship(
        "Content", back_populates="subcontent"
    )
