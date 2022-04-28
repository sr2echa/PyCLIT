import os
import click


class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):
        commands = []
        commands_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))
        for filename in os.listdir(commands_folder):
            if filename.endswith(".py"):
                commands.append(filename.replace(".py", ""))

        commands.sort()
        return commands

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"pyclit.commands.{name}", None, None, ["cli"]) # incase you change the folder name from pyclit, replace "pyclit" with the replaced name in this statement
        except ImportError:
            return
        return mod.cli


@click.command(cls=ComplexCLI) # ComplexCLI Class parses the cmds automatically to Click. So all you have to do is just make new functions in commands folder!
def cli():
    """You have configured PyCLIT properly!""" # Main Help Cmd
    pass
