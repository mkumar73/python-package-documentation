#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pathlib import Path
from setuptools import find_packages, setup

# Package meta-data.
NAME = 'fancy_calcy'
DESCRIPTION = "A toy package for demostrating python package documentation steps."
HOMEPAGE = ""
DOCS = ""

EMAIL = "abc@xyz.com"
AUTHOR = "Manish Kumar"
REQUIRES_PYTHON = ">=3.9.0"

# Load the package's verison file and its content.
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / 'fancy-calcy'
with open(PACKAGE_DIR / "__version__.py") as f:
    version = f.readlines()[-1].split()[-1].strip("\"'")

# ger install_reqs from requirements file, used for setup function later
with open(os.path.join(ROOT_DIR, "requirements.txt")) as f:
    # next(f)
    install_reqs = [line.rstrip() for line in f.readlines()
                    if not line.startswith("#") and not line.startswith("git+")]


# get long description from readme file
with open(os.path.join(ROOT_DIR, "README.md")) as f:
    long_description = f.read()


setup(name=NAME,
      version=version,
      description=DESCRIPTION,
      long_description=long_description,
      long_description_content_type="text/markdown",
      author=AUTHOR,
      author_email=EMAIL,
      python_requires=REQUIRES_PYTHON,
      install_requires=install_reqs,
      license="MIT License",
      packages=find_packages(),
      include_package_data=True,
      keywords=['basf', 'aistore'],
      project_urls={'Homepage:': HOMEPAGE,
                    'Documentation': DOCS}
      )
