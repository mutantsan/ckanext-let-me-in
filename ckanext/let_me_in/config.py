import ckan.plugins.toolkit as tk

CONF_OTL_LINK_TTL = "ckanext.let_me_in.otl_link_ttl"
DEFAULT_OTL_LINK_TTL = 86400


def get_default_otl_link_ttl() -> int:
    """Return a default TTL for an OTL link in seconds."""

    return tk.asint(tk.config.get(CONF_OTL_LINK_TTL, DEFAULT_OTL_LINK_TTL))
