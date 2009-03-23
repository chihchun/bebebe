from google.appengine.ext import db

from gaeo.controller import BaseController

from model.search import SearchLog
from model.user import User
from model.vocabulary import Vocabulary

from dictionary import YahooDictionary
from auth import get_user_or_letlogin

class SearchController(BaseController):

    def index(self):
        word = self.params.get('word')
        if not word:
            raise "no word!"

        user = get_user_or_letlogin(self,'/search/?word=%s' % word)
        log = SearchLog(word=word, user=user)
        log.put()

        voca = Vocabulary(key_name=user.email+'_'+word, word=word, user=user)
        voca.put()

        query_url = YahooDictionary.get_search_url(word)
        self.redirect(query_url)
