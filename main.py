import click
from commands import merge

@click.group()
def cli():
    """A CLI tool to manipulate pdf files"""
    pass

# Add commands to the CLI group
cli.add_command(merge.cmd)


if __name__ == "__main__":
    cli()
