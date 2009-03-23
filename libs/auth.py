from model.user import User

def get_user_or_letlogin(ctrl, dest_url='/'):
    from google.appengine.api import users
    guser = users.get_current_user()
    if not guser:
        ctrl.redirect(users.create_login_url(dest_url))
        return None

    user = User.get_by_key_name(guser.email())
    if not user:
        user = User(key_name=guser.email(), email=guser.email())
        user.put()
    return user
