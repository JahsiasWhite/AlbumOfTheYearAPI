# from setuptools import setup, find_packages
import setuptools

with open("requirements.txt", encoding="utf-8") as f:
    install_requires = f.read().splitlines()

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setuptools.setup(
    name="album-of-the-year-api",
    description="A light weight Python library that acts as an API for the website albumoftheyear.org",
    version="0.2.8",
    license="GNU",
    author="Jahsias White",
    author_email="jahsias.white@gmail.com",
    packages=["albumoftheyearapi"],
    install_requires=install_requires,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JahsiasWhite/AlbumOfTheYearWrapper",
)
