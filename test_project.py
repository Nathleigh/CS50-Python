import pytest
import project


# Create the dict_file as per the project script, so that we can pass it as an argument
dict_file = {}
with open("words.txt") as f:
    for line in f:
        w = line.strip()
        length = len(w)
        dict_file.setdefault(length, []).append(w)

# check that we get a 5-letter word when 5 is specified for length
def test_get_answer():
    a, d = project.get_answer(5)
    assert type(d) == dict
    assert len(a) == 5
    assert a in dict_file[5]


def test_get_guess_valid_input(monkeypatch):
    # Define a mock input for the test
    mock_input = "apple"

    # Use monkeypatch to modify the behavior of input()
    monkeypatch.setattr('builtins.input', lambda _: mock_input)

    # Create a dictionary with word lengths and valid words
    # dict_file = {5: ["apple", "orange", "grapes"]}

    # Call the get_guess function
    result = project.get_guess(5, dict_file)

    # Check if the result matches the mock input
    assert result == mock_input



def test_check_guess_correct_guess(monkeypatch, capsys):
    # Define a mock answer and guess
    answer = "apple"
    guess = "apple"

    # Use monkeypatch to modify the behavior of input()
    monkeypatch.setattr('builtins.input', lambda _: guess)

    # Call the check_guess function
    project.check_guess(guess, answer)

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the correct feedback is printed in green
    assert captured.out == f"\u001b[42;1mA\u001b[0m\u001b[42;1mP\u001b[0m\u001b[42;1mP\u001b[0m\u001b[42;1mL\u001b[0m\u001b[42;1mE\u001b[0m"
