from sqlalchemy import Column, Integer, String, Float, \
    DateTime, Sequence, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Company(Base):
    __tablename__ = 'company'
    
    cik = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String(250))
    sic = Column(Integer)
    gics_sector = Column(String(50))
    gics_subindustry = Column(String(50))
    location = Column(String(50))
    founded_year = Column(String(50))

    securities = relationship('Security', cascade="all, delete-orphan")

    def __repr__(self):
        return "<Company(name='%s')>" % self.name