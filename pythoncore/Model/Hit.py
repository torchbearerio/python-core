from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, JSON
from sqlalchemy.orm import relationship, backref
from Base import Base
import time


class Hit(Base):
    __tablename__ = 'Hits'

    hit_id                          = Column(Integer, primary_key=True)
    pipeline                        = Column(String)
    execution_point_id              = Column(Integer, ForeignKey('ExecutionPoints.execution_point_id'))
    saliency_hit_id                 = Column(String)
    selected_landmark_id            = Column(String, ForeignKey('Landmarks.landmark_id'))
    status                          = Column(String)
    processing_start_time           = Column(TIMESTAMP)
    processing_end_time             = Column(TIMESTAMP)
    timeline                        = Column(JSON)

    candidate_landmarks             = relationship('Landmark', foreign_keys='Landmark.hit_id', backref='hit')
    selected_landmark               = relationship('Landmark', foreign_keys='Hit.selected_landmark_id',
                                                   uselist=False, backref='selected_by')

    def set_start_time_for_task(self, task, time=None):
        if not time:
            time = int(round(time.time() * 1000))
        key = "{task}_start".format(task=task)
        self.timeline = dict((self.timeline if self.timeline else {}).items() + {key: time}.items())

    def set_end_time_for_task(self, task, time=None):
        if not time:
            time = int(round(time.time() * 1000))
        key = "{task}_end".format(task=task)
        self.timeline = dict((self.timeline if self.timeline else {}).items() + {key: time}.items())
