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
- `MakefileParser(makefile_name="Makefile", makefile_path="."` : Primary makefile parser class
    - Class Constructor Parameters
        - makefile_name : Specify the file name of the target Makefile
            + Type: String
            + Default: "Makefile"
        - makefile_path : Specify the file path of the target Makefile
            + Type: String
            + Default: "." (Current Working Directory)

### Functions
- MakefileParser
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

### Data Classes/Types

### Attributes/Variables Objects
- MakefileParser
    - `.makefile_path` : The specified file path of the target Makefile
        + Type: String
    - `.makefile_name` : The specified file name of the target Makefile
        + Type: String

## Usages

### As a library

- Import python package
    ```python
    from mkparse.mkparse import MakefileParser
    ```

- Initialize Variables
    ```python
    # Initialize Variables
    makefile_path = "."
    makefile_name = "Makefile"
    ```

- Initialize Module Classes
    - MakefileParser : The primary makefile file parser
        ```python
        makefile_parser = MakefileParser(makefile_path, makefile_name) # Initialize Makefile Parser
        ```

- Import Makefile file contents into python dictionary (key-value mappings; i.e. HashMap/Associative Array)
    ```python
    # Import Makefile contents into application runtime
    targets, variables = makefile_parser.parse_makefile(makefile_path, makefile_name)
    ```

- Process imported Makefile contents
    ```python
    ```

- Use processed data
    ```python
    print("Targets: {}".format(targets))
    print("Variables: {}".format(variables))
    ```

- Output processed data 
    ```python
    ```

## Resources

## References

## Remarks

