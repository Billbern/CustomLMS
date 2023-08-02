from __future__ import annotations
from typing import List
from datetime import datetime, time
from sqlalchemy import Integer, Text, DateTime, Time, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base
from app.models.question import Question


class Assessment(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    description: Mapped[str] = mapped_column(Text)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    duration: Mapped[time] = mapped_column(Time, nullable=True)
    score: Mapped[int] = mapped_column(Integer, default=0)
    retries: Mapped[int] = mapped_column(Integer, default=0)
    assessment_type: Mapped[Enum] = mapped_column(
        Enum("timed", "nottimed"), default="nottimed"
    )
    questions: Mapped[List[Question]] = relationship(
        "Question", back_populates="assessment_questions"
    )
