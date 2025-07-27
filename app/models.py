from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base

class Jobs:
	__tablename__ = "jobs"

	id = Column(Integer, primary_key=True, index=True)
	title = Column(String, index=True, nullable=False)
	min_salary = Column(Integer)
	max_salary = Column(Integer)
	location = Column(String, nullable=False)
	employer_name = Column(String, nullable=False)

class Users:
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, index=True)
	username = Column(String, index=True, nullable=False)
	password = Column(String, nullable=False)

class AppliedJobs:
	__tablename__ = "appliedjobs"

	id = Column(Integer, primary_key=True, index=True)
	employee_id = Column(Integer, ForeignKey("users.id"))
	job_id = Column(Integer, ForeignKey("jobs.id"))