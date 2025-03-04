import sys
from converter_class import Converter


def get_name():
    """
    This function gets the file name from command-line arguments or user input,
    ensures the file has a valid '.txt' extension.

    Returns:
        str: Validated file name
    """
    if len(sys.argv) == 2:
        name = sys.argv[1]
        if name[-4:] == ".txt" and len(name) >= 5:
            return name
        else:
            sys.exit(
                "Invalid file name. The second command line argument must be 'filename.txt'.")
    elif len(sys.argv) == 1:
        while True:
            name = input("Enter the file name: ")
            if name[-4:] == ".txt" and len(name) >= 5:
                return name
            elif name.lower() == "e":
                sys.exit("You can try again when the files are ready!")
            else:
                print("File name is incorrect. Please enter a valid file name.")
                print("Enter 'E' to exit the program.")
    else:
        sys.exit("Too many command line arguments. Only one file name is allowed.")


def open_file(file):
    """
    Opens the specified text file to ensure it exists.

    Parameters:
        file (str): The file name to open

    Returns:
        str: The validated file name
    """
    try:
        with open(file, "r") as text_file:
            _ = text_file.readlines()
            return file
    except FileNotFoundError:
        sys.exit("File not found. Please check the file and try again.")


def read_lines(file):
    """
    Reads the entire content of a text file.

    Parameters:
        file (str): The file name to read

    Returns:
        str: The text content of the file
    """
    with open(file, "r") as file:
        text = file.read()
        return text


def sorting_option():
    """
    Prompts the user to select a sorting option for word frequency analysis.
    Default is sorting by frequency in descending order.

    Returns:
        str: The sorting method to use
    """
    sorting_option = input("""
Enter the sorting option:
'fd': by frequency in descending order (default)
'fa': by frequency in ascending order
'aa': by words alphabetically in ascending order
'ad': by words alphabetically in descending order
(Press Enter to select the default option)

Your choice: """).strip().lower()

    sorting_options = {
        "fd": "frequency_desc",
        "fa": "frequency_asc",
        "aa": "alpha_asc",
        "ad": "alpha_desc"
    }

    return sorting_options.get(sorting_option, "frequency_desc")


def csv_maker(converter, sort_by):
    """
    Generates a CSV file based on the selected sorting method.

    Parameters:
        converter (Converter): An instance of the Converter class
        sort_by (str): The sorting method to use
    """
    file_names = {
        "frequency_desc": "word_count_freq_desc.csv",
        "frequency_asc": "word_count_freq_asc.csv",
        "alpha_asc": "word_count_alpha_asc.csv",
        "alpha_desc": "word_count_alpha_desc.csv"
    }

    converter.save_to_csv(file_name=file_names[sort_by], sort_by=sort_by)


def main():
    """
    Main function to execute the script workflow.
    1. Get file name.
    2. Open and read file.
    3. Get sorting option from user.
    4. Convert and save results to CSV.
    """
    file_name = open_file(get_name())
    text = read_lines(file_name)
    sort_by = sorting_option()
    converter = Converter(text)
    csv_maker(converter, sort_by)


if __name__ == "__main__":
    main()
