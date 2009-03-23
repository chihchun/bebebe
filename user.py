from google.appengine.ext import db
from gaeo.model import BaseModel

class User(BaseModel):
    name = db.StringProperty(required=True)
    email = db.EmailProperty(required=True)
    profile = db.StringProperty(multiline=True, default='')
    im = db.IMProperty()
    location = db.GeoPtProperty()
    birthdate = db.DateProperty()
    gender = db.IntegerProperty(default=2)
    website = db.LinkProperty()
    friends = db.ListProperty(db.Key)    
    enabled = db.BooleanProperty(default=False)
    created = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)
