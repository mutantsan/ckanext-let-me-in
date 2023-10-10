from __future__ import annotations

from typing import Any, Dict

from ckan.logic.schema import validator_args

Schema = Dict[str, Any]


@validator_args
def lmi_generate_otl(
    ignore_missing,
    unicode_safe,
    user_id_exists,
    user_name_exists,
    user_email_exists,
    int_validator,
    is_positive_integer,
) -> Schema:
    return {
        "uid": [ignore_missing, unicode_safe, user_id_exists],
        "name": [ignore_missing, unicode_safe, user_name_exists],
        "mail": [ignore_missing, unicode_safe, user_email_exists],
        "ttl": [ignore_missing, int_validator, is_positive_integer],
    }
