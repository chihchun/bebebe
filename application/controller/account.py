# -*- coding: utf-8 -*-
from gaeo.controller import BaseController
from gaeo.view.helper.form import date_select

class AccountController(BaseController):
    def signup(self):
        from google.appengine.api import users
        self.guser = users.get_current_user()
        
    def check(self):
        if self._is_xhr:
            from model.user import User
            
            user = User.gql('WHERE name = :1', self.params['name']).get()
            result = {'ok': user is None}
            self.render(json=self.to_json(result))
        else:
            self.render(text='')
            
    def auth(self):
        from model.user import User
        from google.appengine.api import users
        
        guser = users.get_current_user()
        u = User.get_by_key_name(guser.email())
        if u is None:
            self.redirect('/signup')
        else:
            self.session['user'] = {
                'name': u.name,
                'gmail': guser.email()
            }
            self.session.put()
            if self._is_iphone or self._is_android:
                self.redirect('/mobile')
            else:
                self.redirect('/home')
            
        
    def create(self):
        """
        Create the ID
        """
        try:
            # retrieve the parameters
            u = self.params['user']
            
            if len(u['name']) < 2 or len(u['name']) > 16:
                raise 'ID 長度有誤'
                
            from google.appengine.api import users
            from model.user import User
            from model.counter import Counter
            from random import randint
            
            user = User.gql('WHERE name = :1', u['name']).get()
            if user is not None:
                raise 'ID 重覆'
            
            guser = users.get_current_user()
            # create user entity
            user = User(key_name=guser.email(),
                        name=u['name'],
                        email=guser.email())
            user.put()
            
            # add user counter
            shard_name = randint(0, 3)
            counter = Counter.get_by_key_name('user_counter_%d' % shard_name)
            if counter is None:
                counter = Counter(key_name='user_counter_%d' % shard_name, name="user_counter")
            counter.count += 1
            counter.put()
            
            if self.session.has_key('error'):
                del self.session['error']
                self.session.put()
            
            self.redirect('/auth')
        except Exception, ex:
            self.session['error'] = ex
            self.session.put()
            self.redirect('/signup')
            
    def update(self):
        if self._request_method == 'post':
            from model.user import User
            
            user = User.get_by_key_name(self.session['user']['gmail'])

            u = self.params['user']
            d = self.params['date']['select']
            
            website = u['website']
            
            from datetime import date
            from google.appengine.ext import db
            
            user.email = u['email']
            user.profile = u['profile']
            user.gender = int(u['gender'])
            user.birthdate = date(int(d['y']),int(d['m']),int(d['d']))
            if len(u['website']) > 0:
                try:
                    link = db.Link(u['website'])
                    user.website = link
                except:
                    pass
            else:
                user.website = None
            user.put()
            
            self.redirect('/settings?status=updated')
        else:
            self.render(text='Invalid Request')
            
    def signout(self):
        self.session.invalidate()
        self.redirect('/')
