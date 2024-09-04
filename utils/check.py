import click
import os

def check_pdf(path):
    if not os.path.exists(path):
        raise click.BadParameter(f"Input file '{path}' does not exist.")
    if not path.endswith('.pdf'):
        raise click.BadParameter(f"Input file '{path}' is not a PDF file.")


def check_dir(path):
    if path is None or path == '':
        return 
    if not os.path.exists(path):
        click.echo(f"Directory '{path}' does not exist. Creating it now...")
        os.makedirs(os.path.dirname(path))


def check_zip(path):
    if not path.endswith('.zip'):
        raise click.BadParameter(f"Output file '{path}' is not a zip file.")
    