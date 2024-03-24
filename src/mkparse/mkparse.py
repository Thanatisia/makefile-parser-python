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
                        # Remove newline
                        current_target = line[:-1].strip()

                        # Initialize a new entry for the current target
                        targets[current_target] = {"dependencies" : [], "statements" : []}
                    elif current_target:
                        # Check if line defines a new target with/without dependencies (by checking if the last element is ':'
                        if line[:-1][0] == ':':
                            # Split dependencies
                            dependencies = line.split()
                            # Append dependencies to the current target
                            targets[current_target]['dependencies'].extend(dependencies)

                        # Store each row of the target's recipe in its own list
                        targets[current_target]['statements'].append(line.strip())
                    else:
                        # Check if line defines a variable
                        if '=' in line:
                            # Split the '=' to a LHS and RHS
                            parts = line.split(' ')

                            # Validate/Verify parts list is more than or equals to 2 : Name, Operator and Value, value might be empty
                            if len(parts) >= 2:
                                # Strip the newline off the first element which is the variable name
                                variable_name = parts[0].strip()

                                # Obtain Operator
                                operator = parts[1]

                                # Set empty value
                                variable_value = []

                                # Check if variable value is provided
                                if len(parts) >= 3:
                                    # Obtain variable value
                                    variable_value = parts[2:]

                                # Map the variable value to the variable name in the entry mapping
                                variables[variable_name] = {'operator': operator, 'value': variable_value}

                # Close file after usage
                makefile.close()
        except FileNotFoundError:
            print("Makefile not found.")

        return [targets, variables]
    
