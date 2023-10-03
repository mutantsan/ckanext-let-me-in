from __future__ import annotations

from datetime import datetime as dt
from datetime import timedelta as td
from typing import cast

import jwt

import ckan.plugins.toolkit as tk
from ckan import types, model
from ckan.logic import validate

import ckanext.let_me_in.logic.schema as schema
import ckanext.let_me_in.utils as lmi_utils

# import ckanext.let_me_in.model as lmi_model


@validate(schema.lmi_generate_otl)
def lmi_generate_otl(
    context: types.Context, data_dict: types.DataDict
) -> types.ActionResult.AnyDict:
    """Generate a one-time login link for a specified user

    :param user: username of user_id
    :type user: string
    """
    tk.check_access("lmi_generate_otl", context, data_dict)

    user = cast(model.User, model.User.get(data_dict["user"]))
    now = dt.utcnow()
    expires_at = now + td(hours=24)

    token = jwt.encode(
        {"user_id": user.id, "exp": expires_at, "created_at": now.timestamp()},
        lmi_utils.get_secret(True),
        algorithm="HS256",
    )

    # lmi_model.OneTimeLoginToken.create(
    #     {"token": token, "user_id": user.id, "expires_at": expires_at}
    # )

    return {"url": tk.url_for("lmi.login_with_token", token=token, _external=True)}
