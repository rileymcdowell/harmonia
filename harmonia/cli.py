import sys
import click

from harmonia.analysis import conduct_analysis

@click.group()
def cli():
    pass

@cli.command()
@click.argument('chords', nargs=-1)
def analyze(chords):
    if len(chords) == 0:
        click.echo('No chords supplied. Nothing to analyze')
        sys.exit(1)
    else:
        click.echo(conduct_analysis(chords))

if __name__ == '__main__':
    analyze()
