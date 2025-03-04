import pytest
import sys
from project import get_name, open_file, read_lines, sorting_option


def test_get_name(monkeypatch):
    """Tests the get_name function with different inputs, including command-line arguments and user input."""

    # Testing when a valid file name is entered via command-line argument
    monkeypatch.setattr(sys, 'argv', ['project.py', 'sample.txt'])
    assert get_name() == 'sample.txt'

    # Testing when an invalid file name is entered as a command-line argument
    monkeypatch.setattr(sys, 'argv', ['project.py', 'invalidfile'])
    with pytest.raises(SystemExit):
        get_name()

    # Testing interactive input with a valid file name
    monkeypatch.setattr(sys, 'argv', ['project.py'])
    monkeypatch.setattr('builtins.input', lambda _: 'valid_file.txt')
    assert get_name() == 'valid_file.txt'

    # Testing interactive input where user chooses to exit
    monkeypatch.setattr('builtins.input', lambda _: 'e')
    with pytest.raises(SystemExit):
        get_name()


def test_open_file(tmp_path):
    """Tests the open_file function to ensure it correctly handles existing and non-existing files."""

    # Create a temporary text file
    temp_file = tmp_path / "test.txt"
    temp_file.write_text("This is a test file.")

    # Test opening a valid file
    assert open_file(str(temp_file)) == str(temp_file)

    # Test opening a non-existent file (should raise SystemExit)
    with pytest.raises(SystemExit):
        open_file("non_existent_file.txt")


def test_read_lines(tmp_path):
    """Tests the read_lines function to ensure it correctly reads file contents."""

    # Create a temporary text file with multiple lines
    temp_file = tmp_path / "test_read.txt"
    temp_file.write_text("Line 1\nLine 2\nLine 3")

    # Test reading the file content
    content = read_lines(str(temp_file))
    assert content == "Line 1\nLine 2\nLine 3"


@pytest.mark.parametrize("input_value,expected", [
    ("fd", "frequency_desc"),
    ("fa", "frequency_asc"),
    ("aa", "alpha_asc"),
    ("ad", "alpha_desc"),
    ("", "frequency_desc"),  # Default case is gonna be frequency in descending order
    ("invalid", "frequency_desc"),  # Invalid input defaults to "frequency_desc"
])
def test_sorting_option(monkeypatch, input_value, expected):
    """Tests the sorting_option function with various valid and invalid inputs."""
    monkeypatch.setattr('builtins.input', lambda _: input_value)
    assert sorting_option() == expected
