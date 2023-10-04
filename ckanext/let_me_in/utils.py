from __future__ import annotations

from datetime import datetime as dt
from typing import cast

from ckan import model
from ckan.lib.api_token import _get_secret


def get_secret(encode: bool) -> str:
    """Return a secret string for a jwt encode/decode

    We're using an internal func here, ideally, we either need to write a custom
    one or to contribute into CKAN and make it public"""
    return _get_secret(encode)


def get_user(user_id: str) -> model.User:
    """Get a user by its ID/name"""
    return cast(model.User, model.User.get(user_id))


def update_user_last_active(user: model.User) -> None:
    """Update a last_active for a user after we logged him in."""
    user.last_active = dt.utcnow()
    model.Session.commit()
