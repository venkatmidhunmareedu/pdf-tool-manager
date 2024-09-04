import click
import os
from PyPDF2 import PdfReader, PdfWriter
from pdfminer.high_level import extract_text
import pikepdf
from utils.check import check_dir , check_pdf

@click.command(name="encrypt")
@click.option('-i', '--input', help="Input PDF file path", required=True)
@click.option('-p', '--password', help="Password", required=True)
@click.option('-o', '--output', help="Output PDF file path", required=True)
def cmd(input,password,output):
    """Compress PDF files to reduce size while optimizing quality."""
    
    # check if the input files exist
    check_pdf(input)

    # check if the output dir path exists if not create it
    check_dir(os.path.dirname(output))

    # Compress the PDF files and optimize the quality
    with pikepdf.Pdf.open(input) as pdf:
        pdf.save(output, encryption=pikepdf.Encryption(owner=password,user=password,R=4))

    # Print a success message
    click.echo(f"Encryting pdf file : {input} completed and saved to {output}")
