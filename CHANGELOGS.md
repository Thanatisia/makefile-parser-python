# CHANGELOGS

## Table of Contents
+ [2024-03-23](#2024-03-23)
+ [2024-03-24](#2024-03-24)
+ [2024-03-25](#2024-03-25)

## Entry Logs
### 2024-03-23
#### 1552H
+ Initial Commit
+ Version: v0.1.0

- New
    + Added new file '.gitignore'
    + Added new document 'CHANGELOGS.md'
    + Added new document 'README.md'
    + Added new document 'USAGE.md'
    + Added new document 'requirements.txt' : Python packages dependencies
    - Added new directory 'src/' : Contains the project source codes
        + Added new python source file 'main.py' : Simple proof-of-concept implementation and unit test source file
        - Added new directory 'mkparse' : The Makefile-to-Python Parser package
            + Added new source file 'mkparse.py' : The primary Makefile-to-Python Parser Module

#### 1628H
+ Version: v0.2.0

- New
    + Added python packaging script 'setup.py' for setuptools'

- Updates
    - Updated document '.gitignore'
        + Added files
    - Updated source file 'main.py' in 'src/'
        + Fixed formatting

### 2024-03-24
#### 2204H
- Updates
    - Updated source file 'mkparser.py' in 'src/mkparser'
        + Added Makefile parser implementation (to be tested)

#### 2208H
- Updates
    - Updated document 'README.md'
        + Fixed pip install URL

#### 2344H
- New
    - Added new directory 'tests/' for writing unit tests and other tests
        + Added new unit test source 'unittest.py' for holding the main unit tests
        - Added new directory 'resources/' for holding test resource files
            - Added new directory 'Makefiles' for holding Makefile resources
                + Added new test Makefile 'test.Makefile'

- Updates
    - Updated document 'README.md'
        + Added new instruction for installing package in editable local development mode
    - Updated document 'requirements.txt'
        + Added the repository's github link as an installable pip package
    - Updated source file 'main.py' in 'src/'
    - Updated source file 'mkparse.py' in 'src/mkparse'
        + Swapped parameter/argument signatures
        + The variable dictionary now returns the operator (string), and the values (list) mapped to the variable name
        - Fixing implementation of Makefile Parser in 'parse_makefiles();'
            - Target is still bugged
                + Having issues detecting if dependencies is found

### 2024-03-25
#### 1202H
- Updates
    - Updated unit test file 'unittest.py' in 'tests/'
        + Modified to match test requirements
    - Updated source file 'mkparse.py' in 'src/mkparse'
        + Fixed Makefile to Python parser logic - To be tested
        + Wrote documentation comment headers in function
        - Added new function 'export_makefile' to export the target and variable dictionaries into a proper Makefile structure
            + To be tested with print statement first

#### 1335H
- Updates
    - Updated unit test file 'unittest.py' in 'tests/'
        + Modified to match test requirements
    - Updated source file 'mkparse.py' in 'src/mkparse'
        - Fixed function 'export_Makefile'
            + Able to export to a Makefile 
        - TODO
            + To implement reading of comments outside of variables and targets

#### 1430H
+ Version: v0.3.0

- Version Changes
    + Added working Makefile-to-Python import/parser support
    + Added working Python-to-Makefile export function

- TODO Ideas
    + Add comment import such that all comments on the global scope (not tied to any targets) will be retrievable

- Updates
    - Updated source file 'mkparse.py' in 'src/mkparse'
        - Function 'makefile_parse()'
            + Added logical check for comments ('#') and to map that line number to the comment for future use
            + Added 'comments' to the return list
            + Added 'comments' to the documentation multiline docstring
    - Updated document 'USAGE.md'
        + Fixed usage example of 'parse_makefile()': Swapped the argument signatures
        + Updated return list of 'parse_makefile()'
        + Added documentation for function 'export_makefile()'
        + Updated general usage examples

#### 1552H
- New
    + Added new '__init__.py' package/module constructor/initializor script in 'src/mkparse'

- Updates
    - Updated Python packaging script 'setup.py' for setuptools
        + Replaced 'find_packages()' with a statically-defined package structure

#### 1555H
+ Version: 0.3.1

- Version Changes
    + Fixed 'setup.py' python packaging via setuptools

#### 1956H
+ Version: 0.3.2

- Version Changes
    + Fixed 'setup.py' python packaging via setuptools

