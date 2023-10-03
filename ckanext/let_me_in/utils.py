from __future__ import annotations

from typing import cast

from ckan.lib.api_token import _get_secret
from ckan import model


def get_secret(encode: bool) -> str:
    """Return a secret string for a jwt encode/decode

    We're using an internal func here, ideally, we either need to write a custom
    one or to contribute into CKAN and make it public"""
    return _get_secret(encode)


def get_user(user_id: str) -> model.User:
    """Get a user by its ID"""
    return cast(model.User, model.User.get(user_id))
