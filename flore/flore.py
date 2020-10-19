import click

from .facede import facede
from .libraries.yaml import Yaml


@click.group()
def flore_cli():
    """A great option for creating SQL tables in toml format."""


@flore_cli.command(help="create flore folder")
def init():
    facede(Yaml())


@flore_cli.command()
def run():
    """ run script to export your migrations to database """
    click.echo("running...")
