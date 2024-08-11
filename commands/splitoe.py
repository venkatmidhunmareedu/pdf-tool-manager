import click
import os
from PyPDF2 import PdfReader, PdfWriter
import zipfile

@click.command(name="splitoe")
@click.option('-i', '--input', help="Input pdf file path", required=True)
@click.option('-o', '--output', help="Output zip file path", required=True)
def cmd(input, output):
    """Split pdf file into odd and even pages and output as zip file having two pdf files."""
    # Check if the input file extension is .pdf
    if not input.endswith('.pdf'):
        raise click.BadParameter(f"Input file '{input}' must have .pdf extension.")
    # Check if the input file exists
    if not os.path.exists(input):
        raise click.BadParameter(f"Input file '{input}' does not exist.")
    
    # check if the output file extension is .zip
    if not output.endswith('.zip'):
        raise click.BadParameter(f"Output file '{output}' must have .zip extension.")
    # check if the output dir path exists if not create it
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))
    # Define output paths for split PDF files
    odd_pdf_path = "odd_pages.pdf"
    even_pdf_path = "even_pages.pdf"
    
    # Create PdfWriter objects for odd and even pages
    odd_writer = PdfWriter()
    even_writer = PdfWriter()
    
    # Read the input PDF
    reader = PdfReader(input)
    total_pages = len(reader.pages)
    
    # Split the PDF into odd and even pages
    for i in range(total_pages):
        page = reader.pages[i]
        if i % 2 == 0:  # Even index (0-based), corresponds to odd page number (1-based)
            odd_writer.add_page(page)
        else:  # Odd index (0-based), corresponds to even page number (1-based)
            even_writer.add_page(page)
    
    # Write the split PDF files
    with open(odd_pdf_path, "wb") as odd_file:
        odd_writer.write(odd_file)
    with open(even_pdf_path, "wb") as even_file:
        even_writer.write(even_file)
    
    # Create a zip file containing the two PDFs
    with zipfile.ZipFile(output, 'w') as zipf:
        zipf.write(odd_pdf_path, os.path.basename(odd_pdf_path))
        zipf.write(even_pdf_path, os.path.basename(even_pdf_path))
    
    # Clean up temporary PDF files
    os.remove(odd_pdf_path)
    os.remove(even_pdf_path)
    
    # Print a success message
    click.echo(f"Successfully split PDF file '{input}' and saved to '{output}'")
