import os
import pathlib

import click

from .base import Base


class Yaml(Base):
    def create(self):
        migrations_dir = "migrations"

        if not os.path.exists(migrations_dir):
            os.mkdir(migrations_dir)

        for file in ("migration.yaml", "seed.yaml", "config.yaml"):
            file = os.path.join(migrations_dir, file)
            if not os.path.exists(file):
                pathlib.Path(file).touch()
                click.echo(f"{file} created successfully")
            else:
                click.echo("we need create nothing.look like good :)")
                break
