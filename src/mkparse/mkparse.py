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

        :: Output
        - targets: Pass the new targets list you wish to export
            + Type: Dictionary
            - Format
                {
                    "target-name" : {
                        "dependencies" : [your, dependencies, here],
                        "statements" : [your, statements, here]
                    }
                }
            - Key-Value Explanation
                - target-name : Each entry of 'target-name' contains a Makefile build target/instruction/rule 
                    - Key-Value Mappings
                        - dependencies : Specify a list of all dependencies 
                            - Notes: 
                                - Dependencies are the pre-requisite rules to execute before executing the mapped target
                                    - i.e.
                                        [target-name]: [dependencies ...]
                        - statements : Specify a list of all rows of statements to write under the target
        - variables : Pass the new variables list you wish to export
            + Type: Dictionary 
            - Format
                {
                    "variable-name" : {
                        "operator" : "operator (i.e. =|?=|:=)",
                        "value" : [your, values, here]
                    }
                }
            - Key-Value Explanation
                - variable-name : Each entry of 'variable-name' contains a Makefile variable/ingredient
                    - Key-Value Mappings
                        - operator : Specify the operator to map the variable to its value string/array/list
                            + Type: String
                            - Operator Keyword Types
                                + '='
                                + '?='
                                + ':='
                        - value : Specify the value string/array/list (as a list) that you want to map to the variable
                            + Type: List
        - comments : Pass the updated global comments list you wish to export (NOTE: Currently unused; for future development plans)
            + Type: Dictionary 
            - Format
                {
                    "line-number" : comment-from-that-line
                }
            - Key-Value Explanation
                - variable-name : Each entry of 'variable-name' contains a Makefile variable/ingredient
                    - Key-Value Mappings
                        - line-number: The line number; this is mapped to the comment stored at that line
        """
        # Initialize Variables
        targets = {}
        variables = {}
        curr_target = None
        curr_target_name = ""
        line_number = 0
        comments = {} # Store comments here; map line number to the comment

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
                    # line = line.split('#', 1)[0]
                    line = line.rstrip()

                    # Check if line is empty after removing comments
                    if not line:
                        # Line is empty, continue
                        continue

                    # Check if line contains a '#' (a comment)
                    if line[0] == '#':
                        # Store all comments
                        comments[line_number] = line

                    # Check if line contains a '=' (defines a variable)
                    elif '=' in line:
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

                    # Check if line contains ':' (defines a target)
                    elif ':' in line:
                        # Check if line ends with ':' (does not have any dependencies)
                        if line.endswith(':'):
                            # Ends with ':' == there are no dependencies, also is definitely a target
                            curr_target_name = line.split(':')[0].strip()

                            # Initialize a new entry for the current target
                            targets[curr_target_name] = {"dependencies" : [], "statements" : []}
                        else:
                            # Does not end with ':' == there are dependencies

                            # Check if line is really a target and not a statement
                            if not ('\t' in line):
                                # This is a target with dependencies

                                # Split line by ':'
                                curr_target = line.split(':')
                                curr_target_name = curr_target[0].strip()
                                curr_target_dependencies = curr_target[1].strip()

                                # Initialize a new entry for the current target
                                targets[curr_target_name] = {"dependencies" : [], "statements" : []}

                                # Null-value validation
                                if curr_target_dependencies == "":
                                    curr_target_dependencies = None

                                # Remove newline
                                # current_target = line[:-1].rstrip()

                                # Check if dependencies are required
                                if not(curr_target_dependencies == None):
                                    # Are required
                                    # Append dependencies to the current target
                                    targets[curr_target_name]['dependencies'].append(curr_target_dependencies)

                    # Not target = statements, append statements to the target

                    # Check for empty name
                    if not (curr_target_name == '') :
                        # There's tab, a target does not have indentations (means that this is a statement)

                        # Store each row of the target's recipe in its own list
                        targets[curr_target_name]['statements'].append(line.rstrip())

                    # Increment Line Number
                    line_number += 1

                for curr_target_name,curr_target_values in targets.items():
                    # Get current target's dependencies
                    curr_target_dependencies = curr_target_values["dependencies"]

                    # Get current target's statements
                    curr_target_statements = curr_target_values["statements"]

                    # Remove the first line from the list
                    targets[curr_target_name]['statements'] = curr_target_statements[1:]

                # Close file after usage
                makefile.close()
        except FileNotFoundError:
            print("Makefile not found.")

        return [targets, variables, comments]

    def export_Makefile(self, targets:dict, variables:dict, makefile_name="Makefile", makefile_path=".") -> str:
        """
        Export the targets and variables list into an output Makefile

        :: Params
        - targets: Pass the new targets list you wish to export
            + Type: Dictionary
            - Format
                {
                    "target-name" : {
                        "dependencies" : [your, dependencies, here],
                        "statements" : [your, statements, here]
                    }
                }
            - Key-Value Explanation
                - target-name : Each entry of 'target-name' contains a Makefile build target/instruction/rule 
                    - Key-Value Mappings
                        - dependencies : Specify a list of all dependencies 
                            - Notes: 
                                - Dependencies are the pre-requisite rules to execute before executing the mapped target
                                    - i.e.
                                        [target-name]: [dependencies ...]
                        - statements : Specify a list of all rows of statements to write under the target
        - variables : Pass the new variables list you wish to export
            + Type: Dictionary 
            - Format
                {
                    "variable-name" : {
                        "operator" : "operator (i.e. =|?=|:=)",
                        "value" : [your, values, here]
                    }
                }
            - Key-Value Explanation
                - variable-name : Each entry of 'variable-name' contains a Makefile variable/ingredient
                    - Key-Value Mappings
                        - operator : Specify the operator to map the variable to its value string/array/list
                            + Type: String
                            - Operator Keyword Types
                                + '='
                                + '?='
                                + ':='
                        - value : Specify the value string/array/list (as a list) that you want to map to the variable
                            + Type: List
        - makefile_name : Specify the name of the output Makefile to export to
            + Type: String
            + Default Value: "Makefile"
        - makefile_path : Specify the path containing the output Makefile to export to
            + Type: String
            + Default Value: "."

        :: Output
        - File Name: [makefile_path]/[makefile_name]
        - File Type: Makefile
        - Format:
            ```
            [variable-name] = variable values
            [target-name] : your dependencies here
                # Instructions/statements
            ```
        """
        # Initialize Variables
        error_msg = ""
        makefile_fullpath = os.path.join(makefile_path, makefile_name)

        # Check if file exists
        if not (os.path.isfile(makefile_fullpath)):
            # Open file
            with open(makefile_fullpath, "a+") as export_Makefile:
                # Loop through all variables
                for variable_name, variable_mappings in variables.items():
                    # Obtain variable map operator
                    variable_operator = variable_mappings["operator"]

                    # Obtain variable values
                    variable_values = ' '.join(variable_mappings["value"])

                    # Write to Makefile
                    out_str = "{} {} {}\n".format(variable_name, variable_operator, variable_values)
                    export_Makefile.write(out_str)

                export_Makefile.write("\n")

                # Loop through all targets
                for target_name, target_mappings in targets.items():
                    # Obtain target dependencies
                    target_dependencies = ' '.join(target_mappings["dependencies"])

                    # Obtain target statements
                    target_statements = '\n'.join(target_mappings["statements"])

                    # Write to Makefile
                    out_str = "{}: {}\n{}\n".format(target_name, target_dependencies, target_statements)
                    export_Makefile.write(out_str + "\n")

                # Close file after usage
                export_Makefile.close()
        else:
            error_msg = "Makefile {} already exists".format(makefile_fullpath)

        return error_msg

