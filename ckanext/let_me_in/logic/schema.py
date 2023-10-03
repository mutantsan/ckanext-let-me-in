from __future__ import annotations

from typing import Any, Dict

from ckan.logic.schema import validator_args


Schema = Dict[str, Any]


@validator_args
def lmi_generate_otl(not_empty, unicode_safe, user_id_or_name_exists) -> Schema:
    return {"user": [not_empty, unicode_safe, user_id_or_name_exists]}
