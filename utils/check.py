import click
import os

def check_pdf(path):
    if not os.path.exists(path):
        raise click.BadParameter(f"Input file '{path}' does not exist.")
    if not path.endswith('.pdf'):
        raise click.BadParameter(f"Input file '{path}' is not a PDF file.")

