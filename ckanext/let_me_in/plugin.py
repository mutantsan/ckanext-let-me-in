import ckan.plugins as p
import ckan.plugins.toolkit as tk


@tk.blanket.actions
@tk.blanket.cli
@tk.blanket.auth_functions
@tk.blanket.blueprints
@tk.blanket.validators
class LetMeInPlugin(p.SingletonPlugin):
    pass
