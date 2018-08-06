import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tsvdro",
    version="1.0.0",
    author="James E. Dobson",
    author_email="James.E.Dobson@Dartmouth.EDU",
    description="utilities for data-rich humanities objects (DRO)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeddobson/tsvdro",
    packages=['tsvdro'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
