import click
import os
from PyPDF2 import PdfReader, PdfWriter
from pdfminer.high_level import extract_text
import pikepdf

@click.command(name="encryptpdf")
@click.option('-i', '--input', help="Input PDF file path", required=True)
@click.option('-p', '--password', help="Password", required=True)
@click.option('-o', '--output', help="Output PDF file path", required=True)
def cmd(input,password,output):
    """Compress PDF files to reduce size while optimizing quality."""
    
    # Check if the input files exist
    if not os.path.exists(input):
        raise click.BadParameter(f"Input file '{input}' does not exist.")
    if not input.endswith('.pdf'):
        raise click.BadParameter(f"Input file '{input}' is not a PDF file.")
    
    # check if the output file extension is .pdf 
    if not output.endswith('.pdf'):
        raise click.BadParameter(f"Output file '{output}' must have .pdf extension.")
    # check if the output dir path exists if not create it
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))
    

    # Compress the PDF files and optimize the quality
    with pikepdf.Pdf.open(input) as pdf:
        pdf.save(output, encryption=pikepdf.Encryption(owner=password,user=password,R=4))

    # Print a success message
    click.echo(f"Encryting pdf file : {input} completed and saved to {output}")
