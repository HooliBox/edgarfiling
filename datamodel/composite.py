from sqlalchemy import Column, Integer, String, Float, \
    DateTime, Sequence, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Composite(Base):
    __tablename__ = 'composite'
    
    id = Column(Integer, primary_key=True)
    group_id = Column(String(15))
    asof_date = Column(DateTime)
    figi = Column(String(15), ForeignKey('security.figi', onupdate="cascade"))
    weight = Column(Float, nullable=True)
    share = Column(Float, nullable=True)

    security = relationship('Security',  cascade="all, delete-orphan", single_parent=True)

    def __repr__(self):
        return "<Company(name='%s')>" % self.name