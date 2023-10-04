from ckan import model
from ckan.plugins.interfaces import Interface


class ILetMeIn(Interface):
    """Interface to do something on user login via OTL link"""

    def manage_user(self, user: model.User) -> model.User:
        """Accept a user object that will be logged. Only Active user could be
        logged in, so here we could implement user re-activation, for example.

        The user is always exists, otherwise we are not getting here.

        This happend before we are checking for user state and actual login

        Must return a user object
        """
        return user

    def before_otl_login(self, user: model.User) -> None:
        """Allows to do something before we are logging in a user.
        Happens after all checks and `manage_user` method."""
        pass

    def after_otl_login(self, user: model.User) -> None:
        """Allows to do something after we logged in a user."""
        pass
