# Introduction

This repository share the step by step guide to create and host Python package documentation using Sphinx and Readthedocs.

Topics covered in this guide are:

- [Setting up Sphinx](#setting-sphinx)
- [Configuring Sphinx extensions](#configuring-sphinx-extensions)
- [Guide to document Python package](#guide-to-document-python-package)
- [Create documentation modules](#create-documentation-modules)
- [Testing documentation locally](#testing-documentation-locally)
- [Setting up Readthedocs](#setting-up-readthedocs)
- [Hosting documentation on Readthedocs](#hosting-on-readthedocs)
- [Automating documentation build on Readthedocs](#automate-deployment)

I expect that already have a repository with Python package and you want to document it. If not, you can use the sample package provided in this repository. Let's get started.

-----

## [Setting up Sphinx](#setting-sphinx)

Sphinx is a tool that makes it easy to create intelligent and beautiful documentation for Python projects. It is a widely used tool for documenting Python packages. To install Sphinx, run the following command:

```bash
pip install sphinx==6.2.1
```

**Note:** It's alwatys a good practice to specify the version of the package you are installing. Otherwise you may end up with a broken build in future.

In this guide, we will be using `sphinx==6.2.1`


### Create docs directory
Use the following command to create the `docs` directory in the root of your project:

```bash
sphinx-quickstart docs
```

- If you don't specify docs in the above command it will create a `source` folder instead.
- Once run the above command, it will ask you a series of questions. One of the questions will be to separate the source and build directories. You can choose `n` to keep it simple. I personally prefer to keep all the documentation in the same directory. However, it's up to you. 

Benefits of choosing `n`: no need to specify the source directory while building the documentation. Only use the following command to build the documentation:

```bash
cd docs
make html
```
Otherwise, you need to specify the source directory while building the documentation:

```bash
cd docs
sphinx-build source build
```

- Once you have answered all the questions, it will create a `docs` directory with the following structure:

```bash
docs/
    _build/
    _static/
    _templates/
    conf.py
    index.rst
    Makefile
    make.bat
```

- `conf.py` is the main configuration file for Sphinx. It contains all the settings for the documentation. 
- `index.rst` is the main file where you will write the documentation.
- `Makefile` and `make.bat` are the files that contain the commands to build the documentation. 
- `_build` is the directory where the documentation will be built. It will contain the HTML files.
- `_static` and `_templates` are the directories that contain the static files and templates for the documentation. It will be used to store the image files, CSS files, and JavaScript files.

We will make changes to the `conf.py` and `index.rst` files in the next sections.

-----

## [Configuring Sphinx extensions](#configuring-sphinx-extensions)

Sphinx has a lot of extensions that can be used to enhance the documentation. Some of the popular extensions are mentioned in the `requirements_docs.txt` file. You can install them using the following command:

```bash
cd docs
pip install -r requirements_docs.txt
```

Most common extensions are: m2r2, myst-parser, sphinx-rtd-theme, sphinxcontrib-napoleon, sphinx-copybutton, sphinx-autodoc-typehints. Pleas keep in mind that the documentation theme is governed by the theme you provide in the `conf.py` file. In our case we will be using the `sphinx-rtd-theme`. It's included in the `requirements_docs.txt` file. The extension name should be provided in `conf.py` file. We replaced the default theme with `sphinx-rtd-theme`. Please see the details below:

In `conf.py` file, add the following lines to enable the extensions:
```python
html_theme = 'sphinx_rtd_theme'
```

Please make sure the requirements_docs.txt file is present in the `docs` directory. It will be helpful while deploy the documentation on Readthedocs.


Also add the following lines in `conf.py` file to enable these extensions:
```python
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx_copybutton",
    "sphinx_togglebutton",
    "nbsphinx",
    'numpydoc',
    "IPython.sphinxext.ipython_console_highlighting",
    "IPython.sphinxext.ipython_directive",
    "myst_parser",
    "mdinclude",  # custom module
    "sphinx_rtd_theme",
    "sphinx_autodoc_typehints",
]
```
We have already included an extension `myst_parser` and `m2r2` which enable us to use markdown in the documentation. However, some of the configuration does not work by default therefore, we need to add the Python file named `minclude.py`. It's included in the `docs` directory. 

You need to add these lines in the `conf.py` file to include the `mdinclude.py`.
```python
import pathlib
import sys
import os

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("../"))
sys.path.insert(1, os.path.dirname(
    os.path.abspath("../")) + os.sep + "path_to_root_directory")

# in this case path_to_root_directory is fancy_calcy
```

As of now, we installed the required extensions and configured them in the `conf.py` file. We will move to the next section to document the Python package.

-----

## [Guide to document Python package](#guide-to-document-python-package)

There are different Python docstring style guides which could be used. We will be using the Numpydoc style guide. It's a widely used style guide. You can find the details [here](https://numpydoc.readthedocs.io/en/latest/format.html). The package used for this is `numpydoc`. It's included in the `requirements_docs.txt` file.

The other most popular style guide is Google style guide. You can find the details [here](https://google.github.io/styleguide/pyguide.html#doc-function-args) and [here](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

You could also see how the function and classed have been documented in the `fancy_calcy` package. It's included in the `fancy_calcy` directory. It also includes some mathematical formulas and equations. Also, it provided usage of linking one module inside another module as reference.


-----


## [Create documentation modules](#create-documentation-modules)
Now, we have completed the basic setup and also Python code is well documented using the Numpydoc style guide. Let's move to the next section to create the module level documentation in the `docs` directory.

By defualt, the `index.rst` file contains the following content:
```rst
.. fancy-calcy documentation master file, created by
   sphinx-quickstart on Wed Feb 28 23:12:53 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to fancy_calcy's documentation!
=======================================
.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

Consider this as the table of content for the documentation. You can add the modules in the `toctree` directive. Sphinx looks for this file to build the documentation. It will include the modules mentioned in the `toctree` directive. If a module is not mentioned in the `toctree` directive, it will not be included in the documentation.

Let's create some markdown files such as `installation.md`, `about.md`, and `codeofconduct.md`. Now add the following lines in the `index.rst` file to include these markdown files in the documentation:
```rst
.. only new lines are shown here:

.. toctree::
   :name: Getting Started
   :caption: Getting Started
   :maxdepth: 1
   :hidden:

   installation

.. toctree::
   :name: Community
   :caption: Community
   :maxdepth: 1
   :hidden:

   codeofconduct
   about
```

As of now, we have not done anything to bring the docstrings added to the python files in the documentation. We have on option, we create an `api` folder inside the `docs` directory and add all modules and submodules as defined in the Python package.

Like, we have three modules in the `fancy_calcy` package, namely `basics`, `advanced` and `triangle`. Now, let's folder with the same names in the `api` directory. Each module inside these folder will contain the `index.rst` file and `.rst` files for each function and class.

Let's take an example of the `basics` module. It contains one Python c;as We will create the following files in the `api/basics` directory with two files, namely `index.rst` and `BasicOperations.rst`.

The `docs/api/basics/index.rst` file will contain the following content:
```rst
.. -*- mode: rst -*-

.. currentmodule:: fancy_calcy.basics

Basic Operations
=================

This module provides some basic functionalities for calculation.

=================================== =========================================================================
 Functions                            Description
=================================== =========================================================================
:class:`BasicOperations`              Provide class methods for addition, substraction etc.
=================================== =========================================================================

.. toctree::
   :maxdepth: 1
   :hidden:

   BasicOperations
```
This file will used in the main `index.rst` placed inside `docs/` file to include the `basics` module in the documentation. Similarly, we will create the `docs/api/advanced` and `docs/api/triangle` directories with the `index.rst` and `.rst` files for each function and class.

Once these modules are created, you can add these modules in the `docs/index.rst` file to include them in the documentation. You can also add the markdown files in the `index.rst` file to include them in the documentation.
```rst
.. only new lines are shown here:

.. toctree::
   :name: API Docs
   :caption: API Docs
   :maxdepth: 1
   :hidden:

 
   api/basics/index
   api/advanced/index
   api/triangle/index
```

Now, let's add Python examples to the documentation. We create an `examples.rst` file in the `api` directory. It will contain the following content references to the various Python examples included in the `advanced_example.rst` and `simple_example.rst` files. The actual Python files are present in the `examples` directory in the root of the project. Now, include the `examples.rst` file in the `index.rst` file to include it in the documentation.
```rst
.. only new lines are shown here:

.. toctree::
   :name: Examples
   :caption: Examples
   :maxdepth: 1
   :hidden:

   api/examples
```

We are all set to build the documentation. We will move to the next section to test the documentation locally.

## [Testing documentation locally](#testing-documentation-locally)
You can run the following command to build the documentation locally:
```bash
cd docs
make clean
make html
```

Goto the `_build` directory and open the `index.html` file in the browser. You will see the documentation with the modules mentioned in the `toctree` directive.

Check the html rendered documentation, navigate through the different modules and see if the documentation is rendered correctly. If you see any issues, you can fix them and rebuild the documentation using the above command.










