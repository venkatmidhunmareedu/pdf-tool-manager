import click
from commands import merge , splitoe , compress , encryptpdf

@click.group()
def cli():
    """A CLI tool to manipulate pdf files"""
    pass

# Add commands to the CLI group
cli.add_command(merge.cmd)
cli.add_command(splitoe.cmd)
cli.add_command(compress.cmd)
cli.add_command(encryptpdf.cmd)


if __name__ == "__main__":
    cli()
