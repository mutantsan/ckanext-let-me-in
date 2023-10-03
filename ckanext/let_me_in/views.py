from __future__ import annotations

import logging
from datetime import datetime as dt

import jwt

from ckan.plugins import toolkit as tk
from flask import Blueprint

import ckanext.let_me_in.utils as lmi_utils

log = logging.getLogger(__name__)
lmi = Blueprint("lmi", __name__)


@lmi.route("/lmi/<token>")
def login_with_token(token):
    try:
        data = jwt.decode(token, lmi_utils.get_secret(False), algorithms=["HS256"])

        if dt.utcnow() > dt.fromtimestamp(data["exp"]):
            raise (jwt.ExpiredSignatureError)

        tk.login_user(lmi_utils.get_user(data["user_id"]))
        tk.h.flash_success("You have been logged in.")

    except jwt.ExpiredSignatureError:
        tk.h.flash_error(tk._("The login link has expired. Please request a new one."))
    except jwt.DecodeError:
        tk.h.flash_error(tk._("Invalid login link."))
    else:
        return tk.h.redirect_to("user.me")

    return tk.h.redirect_to("user.login")
