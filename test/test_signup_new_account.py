__author__ = 'Arseniy'


def test_signup_new_account(app):
    username = "user1"
    password = "pass"
    app.james.ensure_user_exists(username, password)