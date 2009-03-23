from google.appengine.ext import db
from gaeo.model import BaseModel

class Counter(BaseModel):
    name = db.StringProperty(required=True)
    count = db.IntegerProperty(required=True, default=0)

    @classmethod
    def increase_counter(cls, name):
        counter = cls.get_by_key_name(name)
        if not counter:
            counter = cls(key_name=name, name=name)
        counter.count += 1 
        counter.put()
        return counter
