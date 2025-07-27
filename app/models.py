from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base

class Jobs:
	__tablename__ = "jobs"

	id = Column(Integer, primary_key=True, index=True)