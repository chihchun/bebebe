from google.appengine.ext import db
from gaeo.model import BaseModel, SearchableBaseModel

from model.user import User

from model.counter import Counter

def get_counter_name(word,user=None):
    prefix = "count_word_%s"
    if not user:
        return prefix % word
    else:
        prefix += '_user_%s'
        return prefix % (word, user.email)

class Vocabulary(BaseModel):
    word = db.StringProperty(required=True)
    lang = db.StringProperty(required=True,default="zhTW")
    last_searched_at = db.DateTimeProperty(auto_now_add=True)

    def put(self):
        Counter.increase_counter(get_counter_name(self.word))
        Counter.increase_counter(get_counter_name(self.word,self.user))
        super(Vocabulary, self).put()

    @property
    def count(self):
        return Vocabulary.get_searched_count(self.word,self.user)

    @property
    def searched_total(self):
        return Vocabulary.get_searched_count(self.word)

    @staticmethod
    def get_searched_count(word, user=None):
        count = 0
        for counter in Counter.gql("WHERE name=:1",
                                get_counter_name(word,user)):
            count += counter.count
        return count
  
Vocabulary.belongs_to(User)
