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
@click.argument("user", required=True)
def uli(user: str):
    """Create a one-time login link for a user"""

    try:
        result = tk.get_action("lmi_generate_otl")({"ignore_auth": True}, {"user": user})
    except tk.ValidationError as e:
        return click.secho(e.error_summary, fg="red")

    click.echo()
    click.echo("Your one-time login link has been generated")
    click.secho(result["url"], fg="green")
