from functools import wraps
from flask import g, redirect, url_for


def login_required(func):
    # keep the function information
    @wraps(func)
    def inner(*args, **kwargs):
        if g.user:
            func(*args, **kwargs)
        else:
            return redirect(url_for("auth.login"))
    return inner
