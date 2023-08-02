from __future__ import annotations
from typing import List
from sqlalchemy import Integer, String, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base
from app.models.answer import Answer


class Question(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    question: Mapped[str] = mapped_column(Text, nullable=False)
    score: Mapped[int] = mapped_column(Integer, nullable=False)
    question_type: Mapped[Enum] = mapped_column(
        Enum("multiplechoice", "shortanswer", "essay", "truefalse"),
        default="shortanswer",
    )
    assessment_id: Mapped[int] = mapped_column(Integer, ForeignKey("assessments.id"))
    answers: Mapped[List[Answer]] = relationship(
        "Answer", back_populates="questionanswers"
    )
