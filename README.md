# JSON Compiler

## Overview
The **JSON Compiler** is a simple tool designed to process, validate, and transform JSON data (make it look cleaner to look at). It supports a couple different transformations, such as converting keys to uppercase, adding metadata, and preserving nested structures. This program is usable for a variety of use cases, including API data preparation, JSON normalization, and more.

## Main Parts of The Program
- **Dynamic JSON Handling**: Processes any JSON structure without requiring predefined keys.
- **Transformations**:
  - Recursively converts all JSON keys to uppercase.
  - Adds a timestamp field (`compiledAt`) to the root of the JSON.
- **Very Good Error Handling**: Makes sure invalid JSON files are caught early (Please if you can find and error that doesn't get handled tell me).
- **Ease of Use**: Works without requiring a schema file for validation, I did this to keep it as simple as possible to run.
- **Fast Performance**: Uses `orjson` for quick JSON parsing and serialization. One of my main goals was to keep it lightning quick

## Why This Project is Useful
- **Standardizes JSON**: Makes sure consistent formatting of JSON data, making it easier to process further (I included a very good example with the `test_file.json` then the final version of that being `output.json` just so you can see the difference).
- **Flexible and Generalized**: Handles any JSON input without needing a fixed structure.
- **Optimized for Speed**: Uses the `orjson` library for high-performance JSON operations.

## Installation and Requirements
### Prerequisites
- **Python 3.6+**

### Required Packages
Install the required package using pip:
```bash
pip install orjson
```

### Clone the Repository
```bash
git clone https://github.com/yourusername/json-compiler.git
cd json-compiler
```

## Usage
### Running the Compiler
To use the compiler, provide an input JSON file and specify the output file:
```bash
python json_compiler.py input.json output.json
```

### Example Input (`input.json`)
```json
{
    "person": {
        "name": "Josh",
        "age": 22
    },
    "company": {
        "name": "USM",
        "location": "Maine"
    }
}
```

### Output (`output.json`)
```json
{
    "PERSON": {
        "NAME": "Josh",
        "AGE": 22
    },
    "COMPANY": {
        "NAME": "USM",
        "LOCATION": "Maine"
    },
    "COMPILEDAT": "2024-12-04T18:45:00.123456"
}
```


## How It Works
1. **Load JSON**: Reads the JSON file and parses it using `orjson` for the best performance possible.
2. **Transform JSON**:
   - Keys are converted to uppercase recursively.
   - A `compiledAt` timestamp is added at the root.
3. **Save JSON**: Outputs the transformed JSON to the specified file using `orjson`.


## Error Handling
The program handles the following errors **extrememly** well:
- **Invalid JSON**: If the input file contains malformed JSON, an error is displayed.
- **File Not Found**: If the input file does not exist, an error is shown.

## License
This project is open-source and available under the MIT License.

**Thanks for reading**
