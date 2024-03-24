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

        :: Syntaxes
        :: =======
        :: Makefile variables Format:
            [variable-name] = [values ...]
     
        :: Makefile target/rules Format:
             [target-name]: [dependencies]
                 # statements...
        """
        # Initialize Variables
        targets = {}
        variables = {}
        current_target = None

        # Process and perform data validation + sanitization
        
        ## Use the default Makefile file name if not provided
        if makefile_name == "":
            makefile_name = self.makefile_name

        ## Use the default Makefile file path if not provided
        if makefile_path == "":
            makefile_path = self.makefile_path

        # Try to open the Makefile
        try:
            with open(os.path.join(makefile_path, makefile_name), 'r') as makefile:
                for line in makefile:
                    # Remove comments
                    line = line.split('#', 1)[0]
                    line = line.strip()

                    # Check if line is empty after removing comments
                    if not line:
                        continue

                    # Check if line defines a new target
                    if line.endswith(':'):
                        current_target = line[:-1].strip()
                        targets[current_target] = []
                    elif current_target:
                        # Append dependencies to the current target
                        dependencies = line.split()
                        targets[current_target].extend(dependencies)
                    else:
                        # Check if line defines a variable
                        if '=' in line:
                            parts = line.split('=')
                            variable_name = parts[0].strip()
                            variable_value = '='.join(parts[1:]).strip()
                            variables[variable_name] = variable_value

                # Close file after usage
                makefile.close()
        except FileNotFoundError:
            print("Makefile not found.")

        return targets, variables
    
