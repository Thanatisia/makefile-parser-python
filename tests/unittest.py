"""
Main Runner/Launcher
"""
import os
import sys
from mkparse.mkparse import MakefileParser

def test_Makefile(makefile_name = "Makefile", makefile_path = ".") -> list:
    # Initialize Variables
    makefile_parser = MakefileParser(makefile_name, makefile_path) # Initialize Makefile Parser

    # Import Makefile contents into application runtime
    targets, variables, comments = makefile_parser.parse_makefile(makefile_name, makefile_path)

    # Process imported Makefile contents

    # Use processed data

    # Output processed data
    return [targets, variables, comments]

def test_export_Makefile(targets, variables, makefile_name="Makefile", makefile_path=".") -> None:
    # Initialize Variables
    makefile_parser = MakefileParser(makefile_name, makefile_path) # Initialize Makefile Parser

    # Export Makefile dictionaries to Makefile
    makefile_parser.export_Makefile(targets, variables, makefile_name, makefile_path)

    # Process imported Makefile contents

    # Use processed data

    # Output processed data

def test_format_Makefile(targets, variables, makefile_name="Makefile", makefile_path=".") -> list:
    # Initialize Variables
    makefile_parser = MakefileParser(makefile_name, makefile_path) # Initialize Makefile Parser

    # Format Makefile output into formatted string
    formatted_makefile_Contents = makefile_parser.format_makefile_Contents(targets, variables)

    # Process imported Makefile contents
    formatted_makefile_Targets = formatted_makefile_Contents["targets"]
    formatted_makefile_Variables = formatted_makefile_Contents["variables"]

    # Use processed data

    # Output processed data
    return [formatted_makefile_Targets, formatted_makefile_Variables]

def test_trim_makefile_Contents(targets, variables, makefile_name="Makefile", makefile_path=".") -> list:
    """
    Test trim function 'trim_makefile_contents()'

    Goal: Trim and remove all special characters ("\n", "\t" etc) from the imported file contents
    """
    # Initialize Variables
    makefile_parser = MakefileParser(makefile_name, makefile_path) # Initialize Makefile Parser

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

    # Test Makefile import
    print("Testing Makefile import...")
    targets, variables, comments = test_Makefile(makefile_name, makefile_path)

    print("")

    # Test Makefile data formatting
    print("Testing Makefile data formatting...")
    formatted_makefile_Targets, formatted_makefile_Variables = test_format_Makefile(targets, variables, makefile_name, makefile_path)
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

    # Export Makefile
    print("Testing Export Makefile...")
    err_msg = test_export_Makefile(targets, variables)
    if err_msg != None:
        print("Error during exporting: {}".format(err_msg))
    else:
        print("Export successful")

    print("")

    # Test Makefile trim contents
    print("Testing Makefile content trim...")
    trimmed_makefile_Targets, trimmed_makefile_Variables = test_trim_makefile_Contents(targets, variables, makefile_name, makefile_path)
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

if __name__ == "__main__":
    main()

