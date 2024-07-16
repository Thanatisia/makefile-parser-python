# Usage and Customization

```
Information regarding the various ways to use this Makefile parser
```

## Documentations

### Package
- mkparse

### Modules
- mkparse

### Classes
- `Parser(makefile_name="Makefile", makefile_path="."` : Primary makefile parser class; previously named 'MakefileParser()'
    - Class Constructor Parameters
        - makefile_name : Specify the file name of the target Makefile
            + Type: String
            + Default: "Makefile"
        - makefile_path : Specify the file path of the target Makefile
            + Type: String
            + Default: "." (Current Working Directory)

### Functions
- Parser
    - `.ast_parse(makefile_string_contents=None)`: Makefile parser core unit
        - Parameter/Argument Signatures
            - makefile_string_contents : Specify the Makefile content body (after splitting by newline) you wish to import and parse into the memory buffer
                + Type: String|List
                + Default: ""

        - Return
            + Type: List
            - Values
                - targets: Contains the targets/instructions/rules and the attached dependencies and statements
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
                - variables : Contains the variables and the attached operator (delimiter) and value
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
    - `.parse_makefile(makefile_name="Makefile", makefile_path=".")` : Parse the specified Makefile into python dictionary data objects
        - Parameter/Argument Signatures
            - makefile_name : Specify the file name of the target Makefile
                + Type: String
                + Default: "Makefile"
            - makefile_path : Specify the file path of the target Makefile
                + Type: String
                + Default: "." (Current Working Directory)
        - Return
            + Type: List
            - Values
                + targets   : Makefile rules/targets + dependencies
                + variables : Makefile variables/build arguments
                + comments  : Makefile comments from the global scope (not tied to any targets); Currently unused
    - `.parse_makefile_string(makefile_string="")`: Parse a Makefile syntax string into Python dictionary (Key-Value/HashMap) object
        - Parameter/Argument Signatures
            - makefile_string : Specify the Makefile content body you wish to import and parse into the memory buffer
                + Type: String
                + Default: ""
        - Return
            + Type: List
            - Values
                + targets   : Makefile rules/targets + dependencies
                + variables : Makefile variables/build arguments
                + comments  : Makefile comments from the global scope (not tied to any targets); Currently unused
    - `.export_Makefile(targets:dict, variables:dict, makefile_name="Makefile", makefile_path=".")` : Export the targets and variables list into an output Makefile
        - Parameter/Argument Signatures
            - targets: Pass the new targets list you wish to export
                + Type: Dictionary
                - Format
                    ```python
                    {
                        "target-name" : {
                            "dependencies" : [your, dependencies, here],
                            "statements" : [your, statements, here]
                        }
                    }
                    ```
                - Key-Value Explanation
                    - target-name : Each entry of 'target-name' contains a Makefile build target/instruction/rule 
                        - Key-Value Mappings
                            - dependencies : Specify a list of all dependencies 
                                - Notes: 
                                    - Dependencies are the pre-requisite rules to execute before executing the mapped target
                                        - i.e.
                                            ```make
                                            [target-name]: [dependencies ...]
                                            ```
                            - statements : Specify a list of all rows of statements to write under the target
                                - Examples
                                    ```make
                                    [target-name]:
                                        # Statements...
                                    ```
            - variables : Pass the new variables list you wish to export
                + Type: Dictionary 
                - Format
                    ```python
                    {
                        "variable-name" : {
                            "operator" : "operator (i.e. =|?=|:=)",
                            "value" : [your, values, here]
                        }
                    }
                    ```
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
                + Default Value: "." (Current Working Directory)

        - Output
            + Type: void/null/None
            - Write the provided Makefile specifications to an output Makefile of the following attributes
                + File Name: [makefile_path]/[makefile_name]
                + File Type: Makefile
                - Format:
                    ```
                    [variable-name] = variable values

                    [target-name] : your dependencies here
                        # Instructions/statements
                    ```

    - `.format_makefile_Contents(targets=None, variables=None)`: Format provided makefile targets and variables into content strings
        - Parameter/Argument Signature
            - targets: Specify the Makefile targets to format; Optional
                + Type: Dictionary
                + Default: None
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
            - variables: Specify the Makefile variables to format; Optional
                + Type: Dictionary
                + Default: None
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

        - Return
            - contents: Dictionary (key-value) Mapping of the formatted strings, stored in a list of the targets and variables respectively
                + Type: Dictionary
                - Key-Value mappings
                    - targets : List of all targets formatted into a printable string
                        + Type: List
                    - variables : List of all variables formatted into a printable string
                        + Type: List
                + Format
                    ```python
                    contents = {
                        "targets" : [],
                        "variables" : []
                    }
                    ```
    - `.trim_contents(targets=None, variables=None)` : Trim and remove all special characters ("\n", "\t" etc) from the imported file contents
        - Parameter/Argument Signature
            - targets: Pass the target dictionary mappings you wish to trim/strip; Optional
                + Type: Dictionary
                + Default: None
                - Format
                    ```python
                    {
                        "target-name" : {
                            "dependencies" : [your, dependencies, here],
                            "statements" : [your, statements, here]
                        }
                    }
                    ```
                - Key-Value Explanation
                    - target-name : Each entry of 'target-name' contains a Makefile build target/instruction/rule 
                        - Key-Value Mappings
                            - dependencies : Specify a list of all dependencies 
                                - Notes: 
                                    - Dependencies are the pre-requisite rules to execute before executing the mapped target
                                        - i.e.
                                            [target-name]: [dependencies ...]
                            - statements : Specify a list of all rows of statements to write under the target
            - variables : Pass the target variables mappings you wish to trim/strip; Optional
                + Type: Dictionary 
                + Default: None
                - Format
                    ```python
                    {
                        "variable-name" : {
                            "operator" : "operator (i.e. =|?=|:=)",
                            "value" : [your, values, here]
                        }
                    }
                    ```
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
        - Return: 
            - Default: If both 'targets' and 'variables' are specified
                + Type: List
                - Values
                    + targets   : Trimmed Makefile rules/targets + dependencies
                    + variables : Trimmed Makefile variables/build arguments
            - If only 'variables' is specified
                + Type: Dictionary
                - Values
                    + variables : Trimmed Makefile variables/build arguments
            - If only 'targets' is specified
                + Type: Dictionary
                - Values
                    + targets   : Trimmed Makefile rules/targets + dependencies

### Data Classes/Types

### Attributes/Variables Objects
- Parser
    - `.makefile_path` : The specified file path of the target Makefile
        + Type: String
    - `.makefile_name` : The specified file name of the target Makefile
        + Type: String

## Usages

### As a library

- Import python package
    ```python
    from mkparse.mkparse import Parser
    ```

- Initialize Variables
    ```python
    # Initialize Variables
    makefile_path = "."
    makefile_name = "Makefile"
    ```

- (Optional) Obtain makefile arguments as a CLI argument
    ```python
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
    ```

- Initialize Module Classes
    - Parser : The primary makefile file parser
        ```python
        makefile_parser = Parser(makefile_name, makefile_path) # Initialize Makefile Parser
        ```

- Import Makefile file contents into python dictionary (key-value mappings; i.e. HashMap/Associative Array)
    - Import from a Makefile file
        - Notes
            - If you do not require any of the return objects
                - You can just replace the output object with '_'
                    - i.e.
                        ```python
                        targets, variables, _ = makefile_parser.parse_makefile(makefile_name, makefile_path)
                        ```
        ```python
        # Import Makefile contents into application runtime
        targets, variables, comments = makefile_parser.parse_makefile(makefile_name, makefile_path)
        ```
    - Import using a Makefile string
        ```python
        # Import Makefile string into application runtime
        makefile_string = """# Makefile
        variable = value

        target: dependencies
            # statement
        """
        targets, variables, comments = makefile_parser.parse_makefile_string(makefile_string)
        ```

- Process imported Makefile contents
    - Trim imported Makefile contents
        - Trim both targets and variables
            ```python
            # Trim and remove all special characters ("\n", "\t" etc) from the imported file contents
            targets, variables = makefile_parser.trim_contents(targets, variables)
            ```
        - Trim 'targets' dictionary only
            ```python
            # Trim and remove all special characters ("\n", "\t" etc) from the imported file contents
            targets = makefile_parser.trim_contents(targets=targets)
            ```
        - Trim 'variables' dictionary only
            ```python
            # Trim and remove all special characters ("\n", "\t" etc) from the imported file contents
            variables = makefile_parser.trim_contents(variables=variables)
            ```
    - Format Makefile contents into string
        - Format both 'targets' and 'variables' dictionary
            ```python
            # Format Makefile output into formatted string
            formatted_makefile_Contents = makefile_parser.format_makefile_Contents(targets, variables)

            # Process imported Makefile contents
            formatted_makefile_Targets = formatted_makefile_Contents["targets"]
            formatted_makefile_Variables = formatted_makefile_Contents["variables"]
            ```
        - Format 'targets' dictionary only
            ```python
            # Format Makefile output into formatted string
            formatted_makefile_Contents = makefile_parser.format_makefile_Contents(targets=targets)

            # Process imported Makefile contents
            formatted_makefile_Targets = formatted_makefile_Contents["targets"]
            ```
        - Format 'variables' dictionary only
            ```python
            # Format Makefile output into formatted string
            formatted_makefile_Contents = makefile_parser.format_makefile_Contents(variables=variables)

            # Process imported Makefile contents
            formatted_makefile_Targets = formatted_makefile_Contents["variables"]
            ```

- Use processed data
    ```python
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
    ```

- Output processed data 
    - Export dictionaries to Makefile
        ```python
        # Export Makefile dictionaries to Makefile
        makefile_parser.export_Makefile(targets, variables, makefile_name, makefile_path)       
        ```

## Resources

## References

## Remarks

