from google.appengine.ext import db
from gaeo.model import BaseModel, SearchableBaseModel

from model.user import User
from model.counter import Counter

class SearchLog(BaseModel):
    word = db.StringProperty() 
    lang = db.StringProperty()
    created_at = db.DateTimeProperty(auto_now_add=True) 

SearchLog.belongs_to(User)
