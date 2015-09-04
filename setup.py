import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "PyAnno",
    version = "0.1a",
    author = "Whatever",
    author_email = "andrewjcarter@gmail.com",
    description = "Here we describe what we put in the github repo description ",
    license = "BSD",
    keywords = "labels voting annotation",
    url = "my own webpage",
    packages=['pyanno'],  # This what is really needed, the rest is optional
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)

