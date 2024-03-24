Makefile Parser in Python
=========================

## Information

### Description
+ A simple Makefile Parser written in Python that is designed to simplify the process of importing Makefile contents into python as dictionary (key-value mappings (i.e. hashmap/associative arrays)) objects
+ Standalone CLI add-on support may be considered, but currently, the focus is on a working Makefile-to-Python Parser
+ Currently still a WIP

### Project
+ Package Name: mkparser-python
+ Current Version: v0.2.0

## Setup

*Dependencies*
--------------
+ python3
+ python-pip
+ python3-venv

*Pre-Requisites*
----------------
- Create Python Virtual Environments
    - Generate Virtual Environments
        ```bash
        python3 -m venv [virtual-environment-name]
        ```

    - Chroot into Virtual Environment
        - Linux
            ```bash
            . [virtual-environment-name]/bin/activate
            ```
        - Windows
            ```bash
            .\[virtual-environment-name]\Scripts\activate
            ```

- Install Python Packages/Dependencies
    ```bash
    pip install -Ur requirements.txt
    ```

- Verify packages
    ```bash
    pip freeze list
    ```

*Installing*
------------
- Install locally in development mode
    ```bash
    pip install .
    ```

- Install locally in editable development mode
    ```bash
    pip install -e .
    ```

- Install Python package using GitHub repository via setuptools
    ```bash
    pip install git+https://github.com/Thanatisia/makefile-parser-python
    ```

## Wiki

## Resources

## References

## Remarks

