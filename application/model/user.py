from google.appengine.ext import db
from gaeo.model import BaseModel

class User(BaseModel):
#    name = db.StringProperty(required=True)
    email = db.EmailProperty(required=True)
#    im = db.IMProperty()
    lang = db.StringProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now=True)
