from __future__ import annotations
from typing import List
from datetime import datetime
from sqlalchemy import Integer, String, ForeignKey, Enum, DateTime, func
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base


class Submission(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    date: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=False
    )
    assessment_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("assessments.id"), nullable=False
    )
    comment_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("comments.id"), nullable=True
    )
