# CHANGELOGS

## Table of Contents
+ [2024-03-23](#2024-03-23)
+ [2024-03-24](#2024-03-24)
+ [2024-03-25](#2024-03-25)
+ [2024-03-27](#2024-03-27)
+ [2024-03-28](#2024-03-28)
+ [2024-03-29](#2024-03-29)
+ [2024-03-30](#2024-03-30)

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

#### 2010H
- Updates
    - Updated Python packaging script 'setup.py' for setuptools
        + Testing fix for python packaging via setuptools

#### 2137H
+ Version: 0.3.3

- Version Changes
    + Removed unnecessary prints from 'parse_makefile()'
    + Error message return in 'export_makefile()'
    + Explicit return type definition in 'export_makefile()'

- Updates
    - Updated document 'README.md'
        + Updated version number to 0.3.3
    - Updated Python packaging script 'setup.py' for setuptools
        + Updated version number to 0.3.3
    - Updated source file 'mkparse.py' in 'src/mkparse'
        - Function 'parse_makefile()'
            + Removed 'Sanity Check' print
        - Function 'export_makefile()'
            + Added explicit return type
            + Added error message substitution and return
    - Updated unit test file 'unittest.py' in 'tests/'
        + Added error message output in the test for export_makefile

#### 2217H
+ Version: v0.4.0

- Version Changes
    - mkparse
        + Added new function 'format_makefile_Contents(...)': Function to format the imported targets and variables into printable string then appended into lists of the respective types

- Updates
    - Updated document 'README.md'
        + Updated version number to 0.4.0
    - Updated Python packaging script 'setup.py' for setuptools
        + Updated version number to 0.4.0
    - Updated source file 'mkparse.py' in 'src/mkparse'
        + Added new function 'format_makefile_Contents': Function to format the imported targets and variables into printable string then appended into lists of the respective types
    - Updated unit test file 'unittest.py' in 'tests/'
        + Performed some cleanup
        + Added unit test for 'format_makefile_Contents'
        + Formatted unit tests
    - Updated document 'USAGE.md'
        + Added documentation for function 'format_makefile_Contents()'
        + Added usage examples for the Makefile imported data-into-string formatting

### 2024-03-27
+ Version: v0.4.1

- Version Changes
    - mkparse
        + Added new function 'trim_contents(...)': Function to Trim and remove all special characters ("\n", "\t" etc) from the imported file contents

- Updates
    - Updated document 'README.md'
        + Updated version number to 0.4.1
    - Updated Python packaging script 'setup.py' for setuptools
        + Updated version number to 0.4.1
    - Updated source file 'mkparse.py' in 'src/mkparse'
        + Added new function 'trim_contents(...)': Function to Trim and remove all special characters ("\n", "\t" etc) from the imported file contents
    - Updated unit test file 'unittest.py' in 'tests/'
        + Performed some cleanup
        + Added unit test for 'trim_contents'
        + Formatted unit tests
    - Updated document 'USAGE.md'
        + Added documentation for function 'trim_contents'
        + Fixed documentation for function 'format_makefile_Contents'
        + Added usage examples for function 'trim_contents'

### 2024-03-28
#### 1123H
+ Version: v0.4.2

- Version Changes
    - mkparse
        - Function 'format_makefile_Contents()'
            + Updated to set default value 'None' to parameter/arguments so that developer/user can choose to format either the targets, variables or both

- Updates
    - Updated document 'README.md'
        + Updated version number to 0.4.2
    - Updated Python packaging script 'setup.py' for setuptools
        + Updated version number to 0.4.2
    - Updated source file 'mkparse.py' in 'src/mkparse'
        - Function 'format_makefile_Contents()'
            + Updated to set default value 'None' to parameter/arguments so that developer/user can choose to format either the targets, variables or both
    - Updated unit test source file 'unittest.py' in 'tests/'
        + Added unit test for testing the function 'format_makefile_Contents()': Passing only the Makefile 'targets' dictionary
        + Added unit test for testing the function 'format_makefile_Contents()': Passing only the Makefile 'variables' dictionary

#### 1342H
- Updates
    - Updated source file 'mkparse.py' in 'src/mkparse'
        - Function 'trim_contents()'
            + Attempting to modify function to return results depending on input for dynamic usability

#### 1353H
- Updates
    - Updated unit test source file 'unittest.py' in 'tests/'
        + Added unit test for testing the function 'trim_contents()': Attempting to modify function to return results depending on input for dynamic usability

#### 1401H
- Updates
    - Updated document 'USAGE.md'
        + Updated document with new usage examples and updated parameter explanations

#### 1411H
- Updates
    - Updated document 'USAGE.md'
        - Updated '.trim_contents'
            + Added dynamic return values

#### 1457H
+ Version: v0.4.3

- Version Changes
    - mkparse
        - Function '.format_makefile_Contents()'
            + 'targets' and 'variables' dictionary are now optional inputs
        - Function '.trim_contents()'
            + 'targets' and 'variables' dictionary are now optional inputs
            + Function returns results depending on input for dynamic usability

- Updates
    - Updated document 'README.md'
        + Updated version number to 0.4.3
    - Updated Python packaging script 'setup.py' for setuptools
        + Updated version number to 0.4.3

#### 1942H
- Updates
    - Updated source file 'mkparse.py' in 'src/mkparse'
        - Fixing import bug whereby 'parse_makefile()' is unable to store variable lines without spaces
            - i.e.
                ```makefile
                variable=value
                ```

#### 2043H
- Updates
    - Updated source file 'mkparse.py' in 'src/mkparse'
        - Fixing import bug whereby 'parse_makefile()' is unable to store variable lines without spaces
            + Added additional layer of validation if a variable has no spaces by the delimiter (i.e. 'variable_name=value' instead of 'variable_name = value')
            - Added checks for the keywords ':=', '?=' and ':'
                - Check the variable name (index 1) for the occurence of any of the above keywords
                    + Resize and replace lists if delimiter is obtained

#### 2159H
- Updates
    - Updated source file 'mkparse.py' in 'src/mkparse'
        - Function 'parse_makefile()'
            + Refactored delimiter check

#### 2205H
- Updates
    - Updated source file 'mkparse.py' in 'src/mkparse'
        - Function 'parse_makefile()'
            - Fixing import bug whereby 'parse_makefile()' is unable to store variable lines without spaces
                + Modified positioning and performed cleanup
                + Set operator directly in the operator index checker to obtain the specific various separator ('=', ':=', '?=')

### 2024-03-29
#### 1007H
+ Version: v0.4.4

- Version Changes
    - mkparse
        - Function 'parse_makefile()'
            - Fixed import bug whereby 'parse_makefile()' is unable to store variable lines without spaces
                + Added additional layer of validation if a variable has no spaces by the delimiter (i.e. 'variable_name=value' instead of 'variable_name = value')
                - Added checks for the keywords ':=', '?=' and ':'
                    - Check the variable name (index 1) for the occurence of any of the above keywords
                        + Resize and replace lists if delimiter is obtained

- Updates
    - Updated document 'README.md'
        + Updated version number to 0.4.4.
    - Updated Python packaging script 'setup.py' for setuptools
        + Updated version number to 0.4.4
    - Updated source file 'mkparse.py' in 'src/mkparse'
        - Function 'parse_makefile()'
            - Fixed import bug whereby 'parse_makefile()' is unable to store variable lines without spaces
                + Added additional layer of validation if a variable has no spaces by the delimiter (i.e. 'variable_name=value' instead of 'variable_name = value')
                - Added checks for the keywords ':=', '?=' and ':'
                    - Check the variable name (index 1) for the occurence of any of the above keywords
                        + Resize and replace lists if delimiter is obtained

#### 1116H
- New
    + Added new document 'CONTRIBUTING.md' : Documenting contribution steps

- Updates
    - Updated source file 'mkparse.py' in 'src/mkparse'
        - Function 'parse_makefile()'
            + Fixed the no lines issues
            + Refactored variable positioning 

#### 1118H
+ Version: v0.4.5

- Version Changes
    - mkparse
        - Function 'parse_makefile()'
            - Fixed import bug whereby 'parse_makefile()' is unable to store variable lines without spaces
                + Added additional layer of validation if a variable has no spaces by the delimiter (i.e. 'variable_name=value' instead of 'variable_name = value')
                - Added checks for the keywords ':=', '?=' and ':'
                    - Check the variable name (index 1) for the occurence of any of the above keywords
                        + Resize and replace lists if delimiter is obtained

- New
    + Added new document 'CONTRIBUTING.md' : Documenting contribution steps

- Updates
    - Updated document 'README.md'
        + Updated version number to 0.4.5
    - Updated Python packaging script 'setup.py' for setuptools
        + Updated version number to 0.4.5
    - Updated source file 'mkparse.py' in 'src/mkparse'
        + Performed cleanup
        - Function 'parse_makefile()'
            + Fixed the no lines issues
            + Refactored variable positioning 

#### 1136H
+ Version: v0.4.6

- Version Changes
    - mkparse
        - Function 'parse_makefile()'
            - Added '1' to the 2nd parameter of '.split(delimiter)' to specify a maximum number of searches of occurences of the specified delimiter
                + Basically, the goal is to search for only the first occurence of '=', '?=' or ':=', and if found - thats the delimiter

- Updates
    - Updated document 'README.md'
        + Updated version number to 0.4.6
    - Updated Python packaging script 'setup.py' for setuptools
        + Updated version number to 0.4.6
    - Updated document 'CONTRIBUTING.md'
        + Added new header block 'Debugging' for Debugging snippets
    - Updated source file 'mkparse.py' in 'src/mkparse'
        + Performed cleanup
        - Function 'parse_makefile()'
            - Added '1' to the 2nd parameter of '.split(delimiter)' to specify a maximum number of searches of occurences of the specified delimiter
                + Basically, the goal is to search for only the first occurence of '=', '?=' or ':=', and if found - thats the delimiter

### 2024-03-30
#### 0013H
- Updates
    - Updated document 'USAGE.md'
        - Added documentation for new function 'parse_makefile_string(self, makefile_string="")'
            + Added usage examples 
    - Updated source file 'mkparse.py' in 'src/mkparse' 
        + Added new function `parse_makefile_string(self, makefile_string="")`: To parse Makefile strings into the system without a file
    - Updated unit test file 'unittest.py' in 'tests/'
        + Added unit test for parsing a template Makefile string into system, exporting it for comparison, then pretty printing the containers into standard output

#### 0026H
- Updates
    - Updated document 'USAGE.md'
        + Added documentation for new function 'ast_parse()'
    - Updated source file 'mkparse.py' in 'src/mkparse' 
        + Added new function `ast_parse(self, makefile_string_contents=None)`: The Makefile parser core unit; the parsing will go through this
        + Migrated the parsing functionality of 'parse_makefile_string()' to 'ast_parse()'

