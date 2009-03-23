from google.appengine.ext import db

from gaeo.controller import BaseController

from model.user import User
from model.vocabulary import Vocabulary

from auth import get_user_or_letlogin

class UserController(BaseController):

    def home(self):
        self.user = get_user_or_letlogin(self, '/user/home')
        self.vocabularies = Vocabulary.gql("WHERE user=:1", self.user).fetch(200)
