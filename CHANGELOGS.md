# CHANGELOGS

## Table of Contents
+ [2024-03-23](#2024-03-23)
+ [2024-03-24](#2024-03-24)

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

