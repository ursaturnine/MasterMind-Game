import click
import time

def progressBar(i):
    fill_char = click.style('🔎')
    label_text = click.style("Loading....", fg='green')

    with click.progressbar(
        iterable=i,
        label=label_text,
        fill_char=fill_char,
    ) as items:
        for item in items:
            time.sleep(.1)

