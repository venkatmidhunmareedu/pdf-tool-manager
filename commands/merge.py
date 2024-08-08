import click
import os
from PyPDF2 import PdfReader, PdfWriter

@click.command(name="merge")
@click.option('-i', '--input', help="Input file path",multiple=True, required=True)
@click.option('-o', '--output', help="Output file path",required=True)
def cmd(input, output):
    """Merge pdf files from an end to end"""
    if len(input) < 2:
        raise click.BadParameter("At least two input files are required to merge PDFs.")
    
    # Check if the input files exist
    for file in input:
        if not os.path.exists(file):
            raise click.BadParameter(f"Input file '{file}' does not exist.")
    
    # merge the pdfs 
    pdf_writer = PdfWriter()

    # List of PDF files to be merged - convert the tuple to a list
    pdf_files = list(input)
    for pdf_file in pdf_files:
        # Create a PdfReader object
        pdf_reader = PdfReader(pdf_file)
        # Add each page to the PdfWriter object
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    # Write the merged PDF to a file
    with open(output, 'wb') as output_file:
        pdf_writer.write(output_file)

    # Print a success message
    click.echo(f"Merging PDF files: {', '.join(input)} into {output}")