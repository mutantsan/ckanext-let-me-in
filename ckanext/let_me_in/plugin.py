import ckan.plugins as p
import ckan.plugins.toolkit as tk


@tk.blanket.actions
@tk.blanket.cli
@tk.blanket.auth_functions
@tk.blanket.blueprints
class LetMeInPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        pass
