from sqlalchemy import (
    Boolean,
    Column,
    String,
    DateTime,
    Text,
    Numeric
)
from sqlalchemy.dialects.postgresql import UUID
from db_postgres.baseclass import Base

class SampleData(Base):

    __tablename__ = "sample_data"
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    data_id = Column(UUID(as_uuid=True), primary_key=True)
    data_name = Column(Text)
    data_description = Column(Text)