Contributing Steps
==================

## Table of Contents
+ [Contribution Rules](#contribution-rules)
+ [Contribution Operational Workflow](#contribution-operational-workflow)
+ [Setup](#setup)
+ [Development](#development)
+ [Resources](#resources)
+ [References](#references)
+ [Remarks](#remarks)

## Contribution Rules
+ Please do not push directly to the main branch, always create a Pull Request to merge your fork/branch
- Please write a quality commit message, providing a detailed write-up of your changes
    - At minimum, following the format below
        ```
        Title (Purpose/Reason for change):
        Author Name: 

        Files Changes:
            - file-name-1
            - file-name-2
            - file-name-N

        Change Summary:
            - Description here
        ```

## Contribution Operational Workflow
+ Clone repository and enter local repository directory
+ Create a new branch/fork

## Setup

*Dependencies*
--------------
+ python
+ python-pip
+ python-venv

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

- Initial Setup
    - GitHub (Git Remote Repository Server)
        + Create a fork

    - Clone the repository
        - Notes
            + Change 'Thanatisia' to your account if you created a fork
        ```bash
        git clone https://github.com/Thanatisia/makefile-parser-python
        ```

    - Change directory into local repository
        ```bash
        cd makefile-parser-python
        ```

    - Set git configurations
        - Username
            ```bash
            git config user.name [username]
            ```
        - Email
            ```bash
            git config user.email [email]
            ```


## Development

*Git Workflow*
--------------

> Please perform the following for every changes made

- Create a new git branch
    ```bash
    git checkout -b [new-branch-name]
    ```

- Pull latest changes from the main, development branch(es) or your target branch
    ```bash
    git pull origin [main|development|custom]
    ```

+ Make changes

- Check git status
    ```bash
    git status
    ```

- Check git differences
    ```bash
    git diff
    ```

- Add modified files to your git history and prepare for commit
    ```bash
    git add [files|*|.]
    ```

- Commit all changes made and added
    - Notes
        + Please read [Contribution Rules](#contribution-rules) regarding the quality of commit messages
    ```bash
    git commit -m "[commit-messages]"
    ```

- Push changes made on local repository to your fork/branch in the remote repository server
    ```bash
    git push -u origin [branch-name]
    ```

- When you are ready to create a Pull Request
    - GitHub
        + Go to your branch in your fork
        - Create a Pull Request to merge upstream into the development branch of the main repository
            - Please specify the following
                + Header/Title Subject: `[author-name]: [Purpose/Reason for change]`
                - Body Content
                    ```
                    Date/Time Changed: 
                    Author Name: 

                    Files Changes:
                        - file-name-1
                        - file-name-2
                        - file-name-N

                    Change Summary:
                        - Description here
                    ```
            + Create Pull Request

*Testing Changes*
---------------------
- Uninstall package
    ```bash
    pip uninstall mkparse
    ```

- Install the latest changes in development mode
    ```bash
    pip install .
    ```

- Uninstall and install package in one line
    ```bash
    pip uninstall mkparse; pip install .
    ```

*Debugging*
-----------
- `parse_makefile()`
    - Debugging the splitting of 'variables' into parts
        ```python
        print("Parts: {}".format(parts))
        print("\tVariable Name: {}".format(variable_name))
        print("\tOperator: {}".format(operator))
        print("\tVariable Values: {}".format(variable_value))
        ```

## Resources

## References

## Remarks

