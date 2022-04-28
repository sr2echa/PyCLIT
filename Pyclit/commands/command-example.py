import click
import os

@click.command()
@click.argument('name') # to accept arguments
def cli(name): # name all functions as cli to be the main function
    """Your Sample PyCLIT Command""" # default help output
    click.echo(f"Hello {name}! Welcome to PyCLIT")
