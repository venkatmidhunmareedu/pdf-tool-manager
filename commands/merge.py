import click

@click.command(name="merge")
@click.option('-i', '--input', help="Input file path",multiple=True, required=True)
@click.option('-o', '--output', help="Output file path",required=True)
def cmd(input, output):
    """Merge pdf files from an end to end"""
    if len(input) < 2:
        raise click.BadParameter("At least two input files are required to merge PDFs.")
    click.echo(f"Merging PDF files: {', '.join(input)} into {output}")
