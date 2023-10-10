from __future__ import annotations

import pytest

import ckan.plugins.toolkit as tk
from ckan.tests.helpers import call_action


@pytest.mark.usefixtures("non_clean_db", "with_plugins")
class TestGenerateOTL:
    def test_generate_no_params(self):
        with pytest.raises(
            tk.ValidationError, match="Please, provide uid, name or mail option"
        ):
            call_action("lmi_generate_otl")

    @pytest.mark.usefixtures("clean_db")
    def test_more_than_one_param(self, user):
        with pytest.raises(
            tk.ValidationError,
            match="One param could be used at a time: uid, name or mail",
        ):
            call_action("lmi_generate_otl", uid=user["id"], name=user["name"])

    def test_uid_not_exist(self):
        with pytest.raises(tk.ValidationError, match="Not found: User"):
            call_action("lmi_generate_otl", uid="xxx")

    def test_name_not_exist(self):
        with pytest.raises(tk.ValidationError, match="Not found: User"):
            call_action("lmi_generate_otl", name="xxx")

    def test_mail_not_exist(self):
        with pytest.raises(tk.ValidationError, match="Not found: User"):
            call_action("lmi_generate_otl", mail="xxx")

    @pytest.mark.usefixtures("clean_db")
    def test_by_uid(self, user):
        call_action("lmi_generate_otl", uid=user["id"])

    @pytest.mark.usefixtures("clean_db")
    def test_by_name(self, user):
        call_action("lmi_generate_otl", name=user["name"])

    @pytest.mark.usefixtures("clean_db")
    def test_by_male(self, user):
        call_action("lmi_generate_otl", mail=user["email"])

    @pytest.mark.usefixtures("clean_db")
    def test_ttl_option(self, user):
        call_action("lmi_generate_otl", mail=user["email"])
