import numpy as np

def load_data(fname: str):
    """ Load and return an '.npy' file """
    return np.load(fname)

def find_in_range(data: np.ndarray, num_range: tuple = (0.3, 0.4)):
    """ Return an array containing the values of 'data' that are inside 'num_range' """
    return data[(data > num_range[0]) & (data < num_range[1])]

def first_after_val(data: np.ndarray, val: float = 0.9) -> np.ndarray:
    """ Return the position of the first value larger than val """
    result = np.argwhere(data > val)
    return result[0] if result.size > 0 else None

#####

from hw3_q3 import *
import numpy as np
import pathlib


fname = 'data.npy'
data = np.load(fname)


def test_load_data():
    assert np.all(data == load_data(fname))


def test_find_in_range():
    cur_data = np.load(pathlib.Path('tests_data/find_in_range.npy'))
    assert np.all(cur_data == find_in_range(data))


def test_first_after_val():
    cur_data = np.load(pathlib.Path('tests_data/first_after_val.npy'))
    assert np.all(cur_data == first_after_val(data))


if __name__ == "__main__":
    test_functions = ["test_load_data", "test_find_in_range", "test_first_after_val"]
    errors = []

    for func in test_functions:
        try:
            eval(func)()
        except Exception as e:
            errors.append(f"Failed when testing method '{func}': {e}")
    if len(errors) > 0:
        print(errors)
    else:
        print("Tests pass successfully.")

