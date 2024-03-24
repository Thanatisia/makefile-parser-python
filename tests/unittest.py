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
    targets, variables = makefile_parser.parse_makefile(makefile_name, makefile_path)

    # Process imported Makefile contents

    # Use processed data

    # Output processed data
    return [targets, variables]

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
    targets, variables = test_Makefile(makefile_name, makefile_path)
    print("=======")
    print("Targets")
    print("=======")
    for k,v in targets.items():
        print("{} = ".format(k))
        for curr_target_key, curr_target_value in v.items():
            print("RAW: {} = {}".format(curr_target_key, curr_target_value))
            print("[{}]".format(curr_target_key))
            # Perform type checks
            if type(curr_target_value) == list:
                # List type, print
                for i in range(len(curr_target_value)):
                    # Get current value
                    curr_val = curr_target_value[i]
                    print("\t\t{}".format(curr_val))
            else:
                print("\t\t{}".format(curr_target_value))

    print("")

    print("=========")
    print("Variables")
    print("=========")
    for k,v in variables.items():
        print("{} = {}".format(k,v))

if __name__ == "__main__":
    main()

