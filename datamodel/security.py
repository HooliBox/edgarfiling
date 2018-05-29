from sqlalchemy import Column, Integer, String, Float, \
    DateTime, Sequence, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Security(Base):
    __tablename__ = 'security'
    
    figi = Column(String(15), primary_key=True)
    market_sector = Column(String(20))
    composite_figi = Column(String(15))
    share_class_figi = Column(String(15))
    security_type = Column(String(20))
    security_type2 = Column(String(20))
    unique_id = Column(String(20))
    exch_code = Column(String(2))
    name = Column(String(250))
    ticker = Column(String(20))
    security_description = Column(String(250))
    unique_id_futopt = Column(String(20), nullable=True)
    cik = Column(Integer, ForeignKey('company.cik', onupdate="cascade"))
    
    issuer = relationship('Company',  cascade="all, delete-orphan", single_parent=True, back_populates='securities')

    def __repr__(self):
        return "<Security(name='%s')>" % self.name