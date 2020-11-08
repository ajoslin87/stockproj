import click

def success(message):
    click.echo(click.style(message,fg="blue",bold=True))

def error(message):
    click.echo(click.style(message,fg="red", bold=True))
