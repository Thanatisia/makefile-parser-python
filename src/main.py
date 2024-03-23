"""
Main Runner/Launcher
"""
import os
import sys
from mkparse.mkparse import MakefileParser

def main():
    # Initialize Variables
    makefile_path = "."
    makefile_name = "Makefile"
    makefile_parser = MakefileParser(makefile_path, makefile_name) # Initialize Makefile Parser

    # Import Makefile contents into application runtime
    targets, variables = makefile_parser.parse_makefile(makefile_path, makefile_name)

    # Process imported Makefile contents

    # Use processed data
    print("Targets: {}".format(targets))
    print("Variables: {}".format(variables))

    # Output processed data

if __name__ == "__main__":
    main()

