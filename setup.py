# from setuptools import setup, find_packages
import setuptools

# Runtime deps only (dev/test deps live in requirements.txt for CI).
install_requires = [
    "bs4",
    "curl_cffi>=0.7.0",
]

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")


setuptools.setup(
    name="album-of-the-year-api",
    description="A light weight Python library that acts as an API for the website albumoftheyear.org",
    version="0.2.13",
    license="GNU",
    author="Jahsias White",
    author_email="jahsias.white@gmail.com",
    packages=["albumoftheyearapi"],
    install_requires=install_requires,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JahsiasWhite/AlbumOfTheYearWrapper",
    python_requires=">=3.8",
)
