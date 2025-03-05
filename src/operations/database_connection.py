from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, MetaData, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:password@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
metadata = MetaData()


def get_database():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()


course = Table(
    "course",
    metadata,
    Column("course_id", Integer, primary_key=True, index=True),
    Column("course_title", String, nullable=False),
    Column("duration_hours", Integer, nullable=False)
)

listener = Table(
    "listener",
    metadata,
    Column("listener_id", Integer, primary_key=True, index=True),
    Column("birth_year", Integer, nullable=False),
    Column("sex", String, nullable=False),
    Column("citizenship", String, nullable=False)
)

assignment = Table(
    "assignment",
    metadata,
    Column("assignment_id", Integer, primary_key=True, index=True),
    Column("listener_id", ForeignKey("listener.listener_id"), nullable=False),
    Column("course_id", ForeignKey("course.course_id"), nullable=False),
    Column("additional_educational_program_type", String, nullable=True),
    Column("assignment_status", String, nullable=False),
    Column("department", String, nullable=True),
    Column("education_format", String, nullable=False),
    Column("education_form", String, nullable=True),
    Column("reinstatement", Boolean, nullable=False),
    Column("assignment_date", Date, nullable=False),
    Column("is_an_organization", Boolean, nullable=False),
    Column("organization_name", String, nullable=True),
    Column("study_start", Date, nullable=False),
    Column("study_end", Date, nullable=False),
    Column("price", Integer, nullable=False),
    Column("paid", Integer, nullable=False),
    Column("expulsion_reason", String, nullable=True),
    Column("country", String, nullable=False),
    Column("region", String, nullable=False),
    Column("city", String, nullable=False),
    Column("education", String, nullable=False),
    Column("education_institution", String, nullable=False),
    Column("discipline", String, nullable=False),
    Column("qualification", String, nullable=False),
    Column("listener_category_one", String, nullable=False),
    Column("listener_category_two", String, nullable=True),
    Column("listener_category_three", String, nullable=True),
    Column("tusur_student", Boolean, nullable=False),
    Column("post", String, nullable=True),
    Column("job", String, nullable=True),
    Column("where_had_known_about_course", String, nullable=True)

)


class Course(Base):
    __tablename__ = "course"
    course_id = Column(Integer, primary_key=True, index=True)
    course_title = Column(String, nullable=False)
    duration_hours = Column(Integer, nullable=False)


class Listener(Base):
    __tablename__ = "listener"
    listener_id = Column(Integer, primary_key=True, index=True)
    birth_year = Column(Integer, nullable=False)
    sex = Column(String, nullable=False)
    citizenship = Column(String, nullable=False)


class Assignment(Base):
    __tablename__ = "assignment"
    assignment_id = Column(Integer, primary_key=True, index=True)
    listener_id = Column(ForeignKey("listener.listener_id"), nullable=False)
    course_id = Column(ForeignKey("course.course_id"), nullable=False)
    assignment_status = Column(String, nullable=False)
    additional_educational_program_type = Column(String, nullable=True)
    department = Column(String, nullable=True)
    education_format = Column(String, nullable=False)
    education_form = Column(String, nullable=True)
    reinstatement = Column(Boolean, nullable=False)
    assignment_date = Column(Date, nullable=False)
    is_an_organization = Column(Boolean, nullable=False)
    organization_name = Column(String, nullable=True)
    study_start = Column(Date, nullable=False)
    study_end = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    paid = Column(Integer, nullable=False)
    expulsion_reason = Column(String, nullable=True)
    country = Column(String, nullable=False)
    region = Column(String, nullable=False)
    city = Column(String, nullable=False)
    education = Column(String, nullable=False)
    education_institution = Column(String, nullable=False)
    discipline = Column(String, nullable=False)
    qualification = Column(String, nullable=False)
    listener_category_one = Column(String, nullable=False)
    listener_category_two = Column(String, nullable=True)
    listener_category_three = Column(String, nullable=True)
    tusur_student = Column(Boolean, nullable=False)
    post = Column(String, nullable=True)
    job = Column(String, nullable=True)
    where_had_known_about_course = Column(String, nullable=True)
