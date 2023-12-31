from __future__ import annotations

import logging

import click

import ckan.plugins.toolkit as tk

logger = logging.getLogger(__name__)

__all__ = [
    "letmein",
]


@click.group(short_help="Let me in!")
def letmein():
    pass


@letmein.command()
@click.option("--uid", "-n", default=None, help="User ID")
@click.option("--name", "-u", default=None, help="User name")
@click.option("--mail", "-e", default=None, help="User email")
def uli(uid: str, name: str, mail: str):
    """Create a one-time login link for a user by its ID/name/email"""

    try:
        result = tk.get_action("lmi_generate_otl")(
            {"ignore_auth": True}, {"uid": uid, "name": name, "mail": mail}
        )
    except tk.ValidationError as e:
        return click.secho(e.error_dict, fg="red", err=True)

    click.echo("Your one-time login link has been generated")
    click.secho(result["url"], fg="green")
