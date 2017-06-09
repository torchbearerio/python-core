from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from Base import Base
from pythoncore.utils.setencoder import SetEncoder
import json


class Landmark(Base):
    __tablename__ = 'Landmarks'

    landmark_id               = Column(String, primary_key=True)
    hit_id                    = Column(Integer, ForeignKey('Hits.hit_id'))
    description               = Column(String)
    color                     = Column(String)
    rect                      = Column(String)
    visual_saliency_score     = Column(Float)
    structural_saliency_score = Column(Float)
    position                  = Column(String)

    def get_rect(self):
        return json.loads(self.rect)

    def set_rect(self, r):
        self.rect = json.dumps(r)

    def get_colors(self):
        return json.loads(self.color)

    def set_colors(self, c):
        self.color = json.dumps(c, cls=SetEncoder)
