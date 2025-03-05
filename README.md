# Word Counter
    #### Video Demo:  <https://youtu.be/gVB1_wcaCOo>
    #### Description:

The tool I created processes text files to count word occurrences and produces CSV reports sorted by different criteria. 


## Overview
The Word to CSV Converter project is a Python utility designed to extract, analyze, and export text data from a `.txt` file into a CSV file. The project reads a text file, processes its content to count the frequency of each word, and outputs these results in a structured CSV format. This tool leverages Python’s built-in libraries such as `re` for regular expressions, `csv` for file operations, and `collections.Counter` for counting, as well as the external library `pytest` for testing. 

## Features

- Count word occurrences in text files
- Sort results by:
  - Word frequency (descending or ascending)
  - Alphabetical order (ascending or descending)
- Generate CSV reports with the analyzed data

### Text Extraction and File Handling
1. **File Name Input and Validation:**
   - The project starts by obtaining the file name from either the command-line arguments or via interactive user input.
   - The function `get_name()` validates that the input file name ends with `.txt` and meets a minimum length requirement. If the file name is invalid or the file is not found, the program exits with an appropriate error message.
   
2. **File Reading:**
   - The `open_file()` function checks if the file exists by attempting to open it. If the file is not found, the program halts with a descriptive error.
   - Once validated, the `read_lines()` function reads the entire content of the file and returns it as a string for further processing.

### Processing Text with Regular Expressions and Counter
3. **Word Extraction:**
   - Inside the `Converter` class, the method `process_text()` takes the raw text and uses the `re` module to find all words matching the pattern `\w+`. This pattern matches sequences of alphanumeric characters and ensures that punctuation is ignored.
   - Before matching, the text is converted to lowercase to enable case-insensitive counting.

4. **Counting Words:**
   - The extracted words are fed into the `Counter` class from the `collections` module. `Counter` builds a dictionary-like object where the keys are the words and the values represent their frequencies.
   - For example, a list like `['apple', 'banana', 'apple']` is processed into `{'apple': 2, 'banana': 1}`.

### Sorting the Word Count
5. **Sorting Options:**
   - The project allows multiple sorting strategies to display the results:
     - **Frequency Descending (`frequency_desc`):** Sorts words by frequency from highest to lowest (default).
     - **Frequency Ascending (`frequency_asc`):** Sorts words by frequency from lowest to highest.
     - **Alphabetical Ascending (`alpha_asc`):** Sorts words in alphabetical order from A to Z.
     - **Alphabetical Descending (`alpha_desc`):** Sorts words in reverse alphabetical order from Z to A.
   - The `sorted_word_count()` method implements these options using Python’s built-in `sorted()` function with a lambda function to specify the sorting criteria.

### CSV File Generation
6. **Exporting to CSV:**
   - After sorting the word counts, the `save_to_csv()` method writes the data into a CSV file.
   - It uses the `csv.DictWriter` to write a header row with fields "Word" and "Count" and then writes each word and its corresponding count as rows in the file.
   - The output CSV file is named dynamically based on the chosen sorting option (e.g., `word_count_freq_desc.csv` for frequency descending).

### Command-Line Interface and User Interaction
7. **Interactive and Command-Line Modes:**
   - The project can be run with a command-line argument to specify the file name:
     ```bash
     python project.py sample.txt
     ```
     Alternatively, if no argument is provided, the user will be prompted to enter the file name interactively.
   - The user is then presented with sorting options via the `sorting_option()` function. The input options are:
     - `fd` for frequency descending (default)
     - `fa` for frequency ascending
     - `aa` for alphabetical ascending
     - `ad` for alphabetical descending
   - Invalid inputs default to the frequency descending option.

### Testing and Reliability
8. **Unit Testing with pytest:**
   - My project includes a suite of tests written using `pytest` to ensure that each component behaves as expected.
   - Tests cover:
     - File name validation and proper error handling.
     - Correct functionality of file opening and reading functions.
     - The accuracy of sorting logic for different sorting options.
   - These tests are essential for maintaining reliability and ensuring that future changes do not break core functionality.

## Project Structure
- **converter_class.py:**  
  Contains the `Converter` class and its methods for processing text and exporting CSV files.
- **project.py:**  
  Contains the main workflow, including functions for file input, validation, sorting option selection, and overall orchestration.
- **test_project.py:**  
  Contains the unit tests for the project, ensuring that file handling, text processing, and sorting operate as intended.
- **requirements.txt:**  
  Lists external dependencies. For this project, `pytest` is required as it is the only library not part of Python’s standard library.

## How to Use the Project
1. **Installation:**
   - Ensure you have Python installed on your machine.
   - Install the required external library by running:
     ```bash
     pip install -r requirements.txt
     ```
2. **Running the Converter:**
   - To run the project using a command-line argument:
     ```bash
     python project.py sample.txt
     ```
     Replace `sample.txt` with the name of your text file.
   - To run the project interactively:
     ```bash
     python project.py
     ```
     Then follow the prompts to enter your file name and choose the sorting option.

3. **Output:**
   - After processing, a CSV file will be created in the project directory. The file name reflects the chosen sorting method (e.g., `word_count_alpha_asc.csv`).

## Conclusion
The project I created is an effective example of combining text processing, data manipulation, and file handling in Python. By using regular expressions for word extraction and `Counter` for counting, it efficiently processes textual data. The CSV export functionality makes it easy to analyze and share the word frequency results. Moreover, the use of `pytest` for testing enhances the project’s reliability and maintainability. Whether for educational purposes or practical use, the Word to CSV Converter Project demonstrates robust programming practices and a modular approach to software design.


## Author
Ibrokhim Khakimov
