from __future__ import annotations
from typing import List
from sqlalchemy import Integer, ForeignKey, Text, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base


class Comment(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    comment: Mapped[str] = mapped_column(Text, nullable=False)
    comment_type: Mapped[Enum] = mapped_column(
        Enum("question", "feedback"), default="question"
    )
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=False
    )
    content_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("contents.id"), nullable=True
    )
    assessment_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("assessments.id"), nullable=True
    )
    parent_comment_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("comments.id"), nullable=True
    )
    sub_comments: Mapped[List[Comment]] = relationship("Comment", back_populates="subs")
