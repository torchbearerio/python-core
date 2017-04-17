from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from Base import Base

class ExecutionPoint(Base):
    __tablename__ = 'ExecutionPoints'

    execution_point_id          = Column(Integer, primary_key=True)
    lat                         = Column(DECIMAL(10, 8))
    long                        = Column(DECIMAL(10, 8))
    bearing                     = Column(Integer)
    sample_set                  = Column(String)
    hits                        = relationship('Hit')

