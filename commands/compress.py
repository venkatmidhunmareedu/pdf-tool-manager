import click
import os
from PyPDF2 import PdfReader, PdfWriter
from pdfminer.high_level import extract_text
import pikepdf

@click.command(name="compress")
@click.option('-i', '--input', help="Input PDF file path", required=True)
@click.option('-o', '--output', help="Output PDF file path", required=True)
def cmd(input, output):
    """Compress PDF files to reduce size while optimizing quality."""
    
    # Check if the input files exist
    for file in input:
        if not os.path.exists(file):
            raise click.BadParameter(f"Input file '{file}' does not exist.")
        if not file.endswith('.pdf'):
            raise click.BadParameter(f"Input file '{file}' is not a PDF file.")
    
    # check if the output file extension is .pdf 
    if not output.endswith('.pdf'):
        raise click.BadParameter(f"Output file '{output}' must have .pdf extension.")
    # check if the output dir path exists if not create it
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))
    
    # Initialize PdfWriter to write the compressed PDF
    pdf_writer = PdfWriter()

    # Compress the PDF files and optimize the quality
    for pdf_file in input:
        # Use PyPDF2 to read the PDF
        pdf_reader = PdfReader(pdf_file)
        
        # Process each page in the PDF
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)
            
            # Use pdfminer to extract text (this is optional and for demonstration)
            text = extract_text(pdf_file)
            # You could process text here if needed (e.g., compression, analysis)

    # Save the merged PDF before compressing
    temp_output = "temp_merged.pdf"
    with open(temp_output, 'wb') as output_file:
        pdf_writer.write(output_file)
    
    # Use pikepdf to compress the merged PDF
    with pikepdf.open(temp_output) as pdf:
        # Optimize the PDF with pikepdf
        pdf.save(output, optimize_version=True, compress_streams=True)

    # Clean up the temporary file
    os.remove(temp_output)

    # Print a success message
    click.echo(f"Merged and compressed PDF files: {', '.join(input)} into {output}")
