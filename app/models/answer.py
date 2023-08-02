from __future__ import annotations
from sqlalchemy import Integer, ForeignKey, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base


class Answer(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    answer: Mapped[str] = mapped_column(Text, nullable=False)
    is_correct: Mapped[bool] = mapped_column(Boolean, default=False)
    is_chosen: Mapped[bool] = mapped_column(Boolean, default=False)
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey("questions.id"))
