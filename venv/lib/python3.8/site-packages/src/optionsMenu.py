"""The Options Menu Module Begins the Program


from the src directory, run python optionsMenu.py --help to view console help menu
"""

import click
import constant
from playMasterMindGame import playMasterMind
import time


@click.command()
@click.option('-I', '--instructions', prompt=click.style(constant.INSTRUCTION_MENU, fg="cyan"), type=click.STRING, help="Display Instructions Menu")
def menu(instructions): 
    """This is the options menu. 
    """

    if instructions in constant.USER_YES:
        playMasterMind()
    else:
        click.secho("Goodbye!", fg="magenta", bold=True, italic=True)
        click.secho("Taking You to the GitHub Repo...", fg='bright_green', italic=True)
        time.sleep(3)
        click.launch('https://github.com/ursaturnine/MasterMind-Game')

menu()
