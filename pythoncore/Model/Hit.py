from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from Base import Base


class Hit(Base):
    __tablename__ = 'Hits'

    hit_id                          = Column(Integer, primary_key=True)
    type                            = Column(String)
    execution_point_id              = Column(Integer, ForeignKey('ExecutionPoints.execution_point_id'))
    saliency_hit_id                 = Column(String)
    description_hit_id              = Column(String)
    selected_landmark_id            = Column(String, ForeignKey('Landmarks.landmark_id'))
    distance                        = Column(Integer)
    saliency_reward                 = Column(Integer)
    description_reward              = Column(Integer)
    saliency_assignment_count       = Column(Integer)
    description_assignment_count    = Column(Integer)
    status                          = Column(String)

    candidate_landmarks             = relationship('Landmark', foreign_keys='Landmark.hit_id', backref='hit')
    selected_landmark               = relationship('Landmark', foreign_keys='Hit.selected_landmark_id',
                                                   uselist=False, backref='selected_by')
