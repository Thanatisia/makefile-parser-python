"""
Makefile Parser
"""
import os
import sys

class MakefileParser():
    """
    Makefile - make build system configuration file - parser
    """
    def __init__(self, makefile_name="Makefile", makefile_path="."):
        """
        Class Constructor
        """
        self.makefile_name = makefile_name
        self.makefile_path = makefile_path

    def parse_makefile(self, makefile_name="Makefile", makefile_path=".") -> list:
        """
        Parse Makefile into Python dictionary (Key-Value/HashMap) object
        """
        # Initialize Variables
        targets = {}
        variables = {}

        # Process and perform data validation + sanitization

        ## Use the default Makefile file name if not provided
        if makefile_name == "":
            makefile_name = self.makefile_name

        ## Use the default Makefile file path if not provided
        if makefile_path == "":
            makefile_path = self.makefile_path

        return [targets, variables]


