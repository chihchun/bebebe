from google.appengine.api import users

class Application:
    """
    The base controller init mixin
    """
    def application_init(self):
        """
        default initialization method invoked by dispatcher
        """
        self.login_url = users.create_login_url('/')
        self.logout_url = users.create_logout_url('/')
