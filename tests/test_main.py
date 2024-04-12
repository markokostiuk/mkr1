import os
from datetime import datetime
import pytest
from main import read_file, calculate_price_change

# Fixture to provide test file content
@pytest.fixture
def test_file_content():
    return """good 1, 2024.04.01, 100
good 1, 2024.03.10, 120
good 2, 2024.04.01, 200
"""


# Test read_file function
def test_read_file(test_file_content, tmp_path):
    # Create a temporary file with test content
    test_file = tmp_path / "test_input_data.txt"
    test_file.write_text(test_file_content)

    # Read data from the temporary file
    data = read_file(test_file)

    # Assertions
    assert len(data) == 3
    assert data[0] == ("good 1", datetime(2024, 4, 1), 100)
    assert data[1] == ("good 1", datetime(2024, 3, 1), 120)
    assert data[2] == ("good 2", datetime(2024, 4, 1), 200)

# Test calculate_price_change function
def test_calculate_price_change(test_file_content, tmp_path):
    # Create a temporary file with test content
    test_file = tmp_path / "test_input_data.txt"
    test_file.write_text(test_file_content)

    # Read data from the temporary file
    data = read_file(test_file)

    # Calculate price change for "good 1"
    price_change = calculate_price_change("good 1", data)

    # Assertion
    assert price_change == 20  # Expected price change based on the test data

    # Calculate price change for "good 2"
    price_change = calculate_price_change("good 2", data)

    # Assertion
    assert price_change is None  # No price change for "good 2"

    # Calculate price change for non-existing product
    price_change = calculate_price_change("non-existent product", data)

    # Assertion
    assert price_change is None  # No data available for non-existent product

