# Word Counter
    #### Video Demo:  <URL HERE>
    #### Description:

The tool I created processes text files to count word occurrences and produces CSV reports sorted by different criteria. 

## Features

- Count word occurrences in text files
- Sort results by:
  - Word frequency (descending or ascending)
  - Alphabetical order (ascending or descending)
- Generate CSV reports with the analyzed data

## Installation

1. Clone this repository or download the source files
2. Ensure you have Python 3.x installed
3. No additional dependencies are required beyond the Python standard library, except pytest


### Command Line

Run the program with an optional text file argument:

```bash
python project.py [filename.txt]
```

If no filename is provided, the program will prompt you to enter one.

### Interactive Mode

When running the program without arguments, follow the prompts to:
1. Enter a valid text file name (must end with .txt)
2. Select your preferred sorting method:
   - `fd`: Frequency descending (default)
   - `fa`: Frequency ascending
   - `aa`: Alphabetical ascending
   - `ad`: Alphabetical descending

### Example

```bash
python project.py test.txt
```

After running, select your sorting preference when prompted. The program will generate a CSV file with the word count results.

## Output

The program creates a CSV file with the naming convention:
- `word_count_freq_desc.csv` (for frequency descending)
- `word_count_freq_asc.csv` (for frequency ascending)
- `word_count_alpha_asc.csv` (for alphabetical ascending)
- `word_count_alpha_desc.csv` (for alphabetical descending)

Each CSV contains two columns: "Word" and "Count"

## Project Structure

- `project.py`: Main script that handles user interaction and program flow
- `converter_class.py`: Contains the `Converter` class that processes text and generates reports

## Testing

Tests are included in the `test_project.py` file and can be run using pytest:

```bash
pytest test_project.py
```

Tests cover the main functionality including:
- File name validation
- File operations
- Sorting options

## Author
Ibrokhim Khakimov