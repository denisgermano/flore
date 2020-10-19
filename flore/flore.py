import click


@click.group()
def flore_cli(init, migrate):
    """A great option for creating SQL tables in toml format."""


@flore_cli.command()
def init():
    """ create flore folder """
    click.echo("running...")


@flore_cli.command()
def run():
    """ run script to export your migrations to database """
    click.echo("running...")