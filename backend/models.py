from datetime import datetime
from sqlalchemy import ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column
from pgvector.sqlalchemy import Vector
from database import Base

class Document(Base):
    __tablename__ = "documents"
    id : Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())


class Chunk(Base):
    __tablename__ = "chunks"
    id: Mapped[int] = mapped_column(primary_key=True)
    page: Mapped[int]
    document_id: Mapped[int] = mapped_column(ForeignKey("documents.id"))
    embedding: Mapped[list[float]] = mapped_column(Vector(1536))
    content: Mapped[str] = mapped_column(Text)