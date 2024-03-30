"""
Main Runner/Launcher
"""
import os
import sys
from mkparse.mkparse import Parser

def init(makefile_name="Makefile", makefile_path="."):
    """
    Initialize Global Variables
    """
    global makefile_parser
    makefile_parser = Parser(makefile_name, makefile_path) # Initialize Makefile Parser

def test_Makefile(makefile_name="Makefile", makefile_path=".") -> list:
    # Initialize Variables

    # Import Makefile contents into application runtime
    targets, variables, comments = makefile_parser.parse_makefile(makefile_name, makefile_path)

    # Process imported Makefile contents

    # Use processed data

    # Output processed data
    return [targets, variables, comments]

def test_import_makefile_String(makefile_string="", makefile_name="Makefile", makefile_path="."):
    # Initialize Variables

    # Import Makefile content string into application runtime
    targets, variables, comments = makefile_parser.parse_makefile_string(makefile_string)

    # Process imported Makefile contents

    # Use processed data

    # Output processed data
    return [targets, variables, comments]

def test_export_Makefile(targets, variables, makefile_name="Makefile", makefile_path=".") -> None:
    # Initialize Variables

    # Export Makefile dictionaries to Makefile
    makefile_parser.export_Makefile(targets, variables, makefile_name, makefile_path)

    # Process imported Makefile contents

    # Use processed data

    # Output processed data

def test_format_Makefile(targets, variables) -> list:
    """
    Testing 'format_makefile_Contents()' for both targets and variables
    """
    # Initialize Variables

    # Format Makefile output into formatted string
    formatted_makefile_Contents = makefile_parser.format_makefile_Contents(targets, variables)

    # Process imported Makefile contents
    formatted_makefile_Targets = formatted_makefile_Contents["targets"]
    formatted_makefile_Variables = formatted_makefile_Contents["variables"]

    # Use processed data

    # Output processed data
    return [formatted_makefile_Targets, formatted_makefile_Variables]

def test_format_Makefile_target(targets) -> list:
    """
    Testing 'format_makefile_Contents()' only for the target
    """
    # Initialize Variables

    # Format Makefile output into formatted string
    formatted_makefile_Contents = makefile_parser.format_makefile_Contents(targets=targets)

    # Process imported Makefile contents
    formatted_makefile_Targets = formatted_makefile_Contents["targets"]

    # Use processed data

    # Output processed data
    return formatted_makefile_Targets

def test_format_Makefile_variables(variables) -> list:
    """
    Testing 'format_makefile_Contents()' only for the variables
    """
    # Initialize Variables

    # Format Makefile output into formatted string
    formatted_makefile_Contents = makefile_parser.format_makefile_Contents(variables=variables)

    # Process imported Makefile contents
    formatted_makefile_Variables = formatted_makefile_Contents["variables"]

    # Use processed data

    # Output processed data
    return formatted_makefile_Variables

def test_trim_makefile_Contents(targets, variables) -> list:
    """
    Test trim function 'trim_makefile_contents()'

    Goal: Trim and remove all special characters ("\n", "\t" etc) from the imported file contents
    """
    # Initialize Variables

    # Format Makefile output into formatted string
    trimmed_targets, trimmed_variables = makefile_parser.trim_contents(targets, variables)

    # Process imported Makefile contents
    formatted_makefile_Contents = makefile_parser.format_makefile_Contents(trimmed_targets, trimmed_variables)

    # Process imported Makefile contents
    formatted_trimmed_Targets = formatted_makefile_Contents["targets"]
    formatted_trimmed_Variables = formatted_makefile_Contents["variables"]

    # Use processed data

    # Output processed data
    return [formatted_trimmed_Targets, formatted_trimmed_Variables]

def test_trim_makefile_Targets(targets) -> list:
    """
    Test trim function 'trim_makefile_contents()' for targets only

    Goal: Trim and remove all special characters ("\n", "\t" etc) from the imported file contents
    """
    # Initialize Variables

    # Format Makefile output into formatted string
    trimmed_targets = makefile_parser.trim_contents(targets=targets)

    # Process imported Makefile contents
    formatted_makefile_Contents = makefile_parser.format_makefile_Contents(targets=trimmed_targets)

    # Process imported Makefile contents
    formatted_trimmed_Targets = formatted_makefile_Contents["targets"]

    # Use processed data

    # Output processed data
    return formatted_trimmed_Targets

def test_trim_makefile_Variables(variables) -> list:
    """
    Test trim function 'trim_makefile_contents()' for targets only

    Goal: Trim and remove all special characters ("\n", "\t" etc) from the imported file contents
    """
    # Initialize Variables

    # Format Makefile output into formatted string
    trimmed_variables = makefile_parser.trim_contents(variables=variables)

    # Process imported Makefile contents
    formatted_makefile_Contents = makefile_parser.format_makefile_Contents(variables=trimmed_variables)

    # Process imported Makefile contents
    formatted_trimmed_Variables = formatted_makefile_Contents["variables"]

    # Use processed data

    # Output processed data
    return formatted_trimmed_Variables

def main():
    """
    Unit Test launcher
    """
    # Initialize Variables
    exec = sys.argv[0]
    argv = sys.argv[1:]
    argc = len(argv)
    makefile_path = "."
    makefile_name = "Makefile"

    # Get Arguments
    if argc >= 2:
        makefile_path = argv[0]
        makefile_name = argv[1]

    init(makefile_name, makefile_path)

    # Test Makefile import
    print("Testing Makefile import...")
    targets, variables, comments = test_Makefile()

    print("")

    # Test Makefile data formatting
    print("Testing Makefile data formatting...")
    formatted_makefile_Targets, formatted_makefile_Variables = test_format_Makefile(targets, variables)
    print("=========")
    print("Variables")
    print("=========")
    for i in range(len(formatted_makefile_Variables)):
        # Get current line
        curr_line = formatted_makefile_Variables[i]
        # Print
        print(curr_line)

    print("")

    print("=======")
    print("Targets")
    print("=======")
    for i in range(len(formatted_makefile_Targets)):
        # Get current line
        curr_line = formatted_makefile_Targets[i]
        # Print
        print(curr_line)

    print("")

    # Testing 'format_makefile_Contents()' only for the target
    print("Testing 'format_makefile_Contents()' only for the target...")
    formatted_makefile_Targets = test_format_Makefile_target(targets)

    print("=======")
    print("Targets")
    print("=======")
    for i in range(len(formatted_makefile_Targets)):
        # Get current line
        curr_line = formatted_makefile_Targets[i]
        # Print
        print(curr_line)

    print("")

    # Testing 'format_makefile_Contents()' only for the variables
    print("Testing 'format_makefile_Contents()' only for the variables...")
    formatted_makefile_Variables = test_format_Makefile_variables(variables)

    print("=========")
    print("Variables")
    print("=========")
    for i in range(len(formatted_makefile_Variables)):
        # Get current line
        curr_line = formatted_makefile_Variables[i]
        # Print
        print(curr_line)

    print("")

    # Export Makefile
    print("Testing Export Makefile...")
    err_msg = test_export_Makefile(targets, variables)
    if err_msg != None:
        print("Error during exporting: {}".format(err_msg))
    else:
        print("Export successful")

    print("")

    # Resetting
    print("Resetting...")
    targets, variables, comments = test_Makefile()

    print("")

    # Test Makefile trim contents for targets and variables
    print("Testing Makefile content trim...")
    trimmed_makefile_Targets, trimmed_makefile_Variables = test_trim_makefile_Contents(targets, variables)
    print("=========")
    print("Variables")
    print("=========")
    for i in range(len(trimmed_makefile_Variables)):
        # Get current line
        curr_line = trimmed_makefile_Variables[i]
        # Print
        print(curr_line)

    print("")

    print("=======")
    print("Targets")
    print("=======")
    for i in range(len(trimmed_makefile_Targets)):
        # Get current line
        curr_line = trimmed_makefile_Targets[i]
        # Print
        print(curr_line)

    print("")

    # Resetting
    print("Resetting...")
    targets, variables, comments = test_Makefile()

    # Test Makefile trim contents for targets only
    print("Testing Makefile content trim for Targets only...")
    trimmed_makefile_Targets = test_trim_makefile_Targets(targets)

    print("=======")
    print("Targets")
    print("=======")
    for i in range(len(trimmed_makefile_Targets)):
        # Get current line
        curr_line = trimmed_makefile_Targets[i]
        # Print
        print(curr_line)

    print("")

    # Resetting
    print("Resetting...")
    targets, variables, comments = test_Makefile()

    print("")

    # Test Makefile trim contents for variables only
    print("Testing Makefile content trim for Variables only...")
    trimmed_makefile_Variables = test_trim_makefile_Variables(variables)
    print("=========")
    print("Variables")
    print("=========")
    for i in range(len(trimmed_makefile_Variables)):
        # Get current line
        curr_line = trimmed_makefile_Variables[i]
        # Print
        print(curr_line)

    print("")

    # Test Makefile string import
    print("Testing Makefile string import...")
    makefile_str = """# Makefile
# for Building from Source

### Build Info
CC = your-cross-compiler (i.e. make|ninja etc)
CFLAGS = your-cross-compilation-flags
DEPENDENCIES = your-dependencies-here

### Package Information
PKG_AUTHOR = author-name
PKG_NAME = package-name
BIN_NAME = binaries and executables
SRC_URL = https://github.com/$(PKG_AUTHOR)/$(PKG_NAME)
INSTALL_PATH = installation-path (Default: /usr/local)
CONFIGURE_OPTS = "--prefix=$(INSTALL_PATH)"

### System Information
EDITOR=vim
SHELL := /bin/bash
.PHONY := help install-dependencies setup build install uninstall clean enter
.DEFAULT_RULES := help

## Recipe/Targets
help:
	## Display help message
	@echo -e "[+] help  : Display Help message"
	@echo -e "[+] install-dependencies : Install system packages"
	@echo -e "[+] clone : Clone repository if doesnt exist and initialize submodules"
	@echo -e "[+] configure : Configure the repository source files before building"
	@echo -e "[+] setup : Setup pre-requisites"
	@echo -e "[+] build : Compile/Build everything"
	@echo -e "[+] build-all : Build the project from Source"
	@echo -e "[+] build-doc : Build the project documentations from Source"
	@echo -e "[+] install: Install everything to the host system"
	@echo -e "[+] install-bin : Install and move the compiled binary to the host system"
	@echo -e "[+] install-html : Install HTML to the host system"
	@echo -e "[+] install-doc : Install documentations to the host system"
	@echo -e "[+] uninstall : Uninstall and remove the installed files from the host system"
	@echo -e "[+] clean : Clean/Remove all temporarily-generated files from repository"
	@echo -e "[+] enter : Enter the package repository"

install-dependencies:
	## Install dependencies
	@apt update && apt upgrade && apt install ${DEPENDENCIES}

clone:
	### Clone repository if doesnt exist and initialize submodules
	@test -d ${PKG_NAME} || git clone "${SRC_URL}" && cd ${PKG_NAME}; \\
		# Initialize git submodule contents
		## 2>&1 : Redirect stderr to stdout
		echo -e "Initializing git submodules..."; git submodule init 2>&1; \\
		# Update and clone all git submodules recursively
		echo -e "Cloning all git submodules..."; git submodule update --recursive 2>&1

configure: clone
	## Configure the repository source files before building
	@cd ${PKG_NAME}; ${CC} configure && ./configure ${CONFIGURE_OPTS}

setup: clone configure
	## Setup and perform pre-requisites

build: build-all build-doc
	## Compile/Build everything

build-all: setup
    ## Compile and Build/make the source code into an executable
	@cd ${PKG_NAME}; ${CC} ${CFLAGS} all && \\
		echo -e "[+] Compilation Successful." || \\
		echo -e "[-] Compilation Error."

build-doc: setup
	## Compile and Build documentations
	@cd ${PKG_NAME}; ${CC} ${CFLAGS} doc && \\
		echo -e "[+] Compilation Successful." || \\
		echo -e "[-] Compilation Error."

install: install-bin install-html install-doc
	## Install everything to the host system

install-bin: clone
    ## Install and move the compiled binary to the host system
	@cd ${PKG_NAME}; ${CC} ${CFLAGS} install && \\
        echo -e "[+] Executable Installation Successful." || \\
        echo -e "[-] Executable Installation Error."

install-html: clone
	## Install HTML to the host system
	@cd ${PKG_NAME}; ${CC} ${CFLAGS} install-html && \\
        echo -e "[+] HTML Documentations Installation Successful." || \\
        echo -e "[-] HTML Documentations Installation Error."

install-doc: clone
	## Install documentations to the host system
	@cd ${PKG_NAME}; ${CC} ${CFLAGS} install-doc && \\
		echo -e "[+] Documentations Installation Successful." || \\
		echo -e "[+] Documentations Installation Error."

uninstall: clone
    ## Uninstall and remove installed files from the host system
    ### Uninstall a binary
	@rm /usr/local/bin/{binaries,here,...}
    ### Uninstall a directory
	@test -d /usr/local/[directory] && rm -r /usr/local/[directory]
    ### Uninstall manuals (man1)
	@rm /usr/local/share/man/man1/[manual].1
    ### Uninstall manuals (man3)
	@rm /usr/local/share/man/man3/[manual].3pm
    ### Uninstall manuals (man5)
	@rm /usr/local/share/man/man5/[manual]*
    ### Uninstall manuals (man7)
	@rm /usr/local/share/man/man7/[manual]*

clean: clone
	## Cleanup and remove temporary files generated during compilation
	@cd ${PKG_NAME}; ${CC} clean && \\
        echo -e "[+] Cleanup Successful." || \\
        echo -e "[-] Cleanup Error."

enter: clone
	## Enter the package repository
	@cd ${PKG_NAME};
    """
    targets, variables, comments = test_import_makefile_String(makefile_str, makefile_name, makefile_path)
    print("Targets: {}".format(targets))
    print("Variables: {}".format(variables))
    # Export the generated Makefile
    test_export_Makefile(targets, variables, makefile_name="test-export.Makefile")
    # Format the generated Makefile into human-readable standard output
    formatted_makefile_Targets, formatted_makefile_Variables = test_format_Makefile(targets, variables)
    print("=========")
    print("Variables")
    print("=========")
    for i in range(len(formatted_makefile_Variables)):
        # Get current line
        curr_line = formatted_makefile_Variables[i]
        # Print
        print(curr_line)

    print("")

    print("=======")
    print("Targets")
    print("=======")
    for i in range(len(formatted_makefile_Targets)):
        # Get current line
        curr_line = formatted_makefile_Targets[i]
        # Print
        print(curr_line)

    print("")

if __name__ == "__main__":
    main()

