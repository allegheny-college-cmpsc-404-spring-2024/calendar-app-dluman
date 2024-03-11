# CMPSC 404: Web Applications

This repository houses files for building a calendar application from our Figma mock-up using `flask` and, eventually,
`htmx`.

The `requirements.txt` file describes relevant dependencies (namely `flask`); you must install this module in order
to successfully build and run the platform.

## Creating a virtual environment

Traditionally, when developing Python programs, developers use `virtual environments` (`venv`) to isolate the system under
construction from system Python libraries. We should do the same. Most Python distributions include the ability
to create `venv` out of the box. In the folder containing this repository:
```bash
python -m venv .contacts
```
This creates a folder named `.contacts` which contains the files necessary to separate this application from other system
Python utilities. However, we're not _in_ the environment yet. To start it:

|Operating System |Command |
|:----------------|:-------|
|Windows          |`.venv\Scripts\activate`|
|Apple/Debian Unixes |`. .venv/bin/activate`|

This should render a prefix before your project directory which resembles the terminal prompt:
```
(.contacts) dluman@toaster:~/cmpsc404/building-web-applications
```
Before working on this application, ensure that the `venv` has started, else you'll be missing software that serves the platform.
## Installing project dependencies

To install all of the requirements/dependencies for this project:
```bash
python -m pip install -r requirements.txt
```
