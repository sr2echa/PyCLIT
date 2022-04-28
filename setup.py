from setuptools import setup, find_packages
import json

with open('config.json') as f:
    config=json.loads(f)
	

def requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name="PyCLIT",
    description="A Python CLI Starter Template",
    version="0.1",
    author="Sreecharan S. <sreecharansiva@gmail.com>",
    packages=find_packages(),
    install_requires=requirements(),
    entry_points={
        "console_scripts": [
            f"{config["name"]} = Pyclit.cli:cli"
        ]
    },
)
