from __future__ import annotations

from typing import cast

import pytest

import ckan.model as model
from ckan.tests.helpers import call_action


@pytest.mark.usefixtures("non_clean_db")
class TestOTLViews(object):
    def test_login_user_with_otl(self, app, user):
        otl = call_action("lmi_generate_otl", uid=user["id"])

        result = app.get(otl["url"], status=200)
        assert "You have been logged in" in result.text

        result = app.get(otl["url"], status=200)
        assert (
            "You have tried to use a one-time login link that has expired"
            in result.text
        )

    def test_user_login_expires_the_otl(self, app, user):
        """We are not creating any entity for OTL. It expires right after the
        user it was created for is logged in. This triggers the update of
        `last_active` field and if the OTL is older than this, it will be invalidated"""
        otl = call_action("lmi_generate_otl", uid=user["id"])

        user = cast(model.User, model.User.get(user["id"]))
        user.set_user_last_active()

        result = app.get(otl["url"], status=200)
        assert (
            "You have tried to use a one-time login link that has expired"
            in result.text
        )
