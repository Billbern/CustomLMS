from __future__ import annotations
from typing import List
from datetime import datetime
from sqlalchemy import Integer, ForeignKey, Enum, DateTime, func, Boolean, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base


class UserEnrollment(Base):
    cancellation_reason: Mapped[str] = mapped_column(Text)
    cancelled: Mapped[bool] = mapped_column(Boolean, default=False)
    enrollment_date: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    enrolled_as: Mapped[Enum] = mapped_column(
        Enum("student", "tutor"), default="student"
    )
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    program_id: Mapped[int] = mapped_column(Integer, ForeignKey("programs.id"))
