from pathlib import Path

class FolderIterator:
    def __init__(self, foldername='base'):
        self.foldername = Path(__file__).parent / foldername
        self.uniques = []
        self.duplicates = {}
        self._seen_contents = []
        self._parents = []

    def iter_folder(self):
        for path in self.foldername.rglob("*"):
            if path.is_file():
                try:
                    content = path.read_text(errors='ignore').lower()
                except Exception:
                    continue  # Skip unreadable files

                if content not in self._seen_contents:
                    self._seen_contents.append(content)
                    self._parents.append(path.name)
                    self.uniques.append((path.name, content))

                else:
                    parent_index = self._seen_contents.index(content)
                    parent_name = self._parents[parent_index]
                    if parent_name not in self.duplicates:
                        self.duplicates[parent_name] = []
                    self.duplicates[parent_name].append(path.name)




########################
import pathlib

from hw3_q1 import *


def test_using_pathlib():
    fi = FolderIterator()
    assert isinstance(fi.foldername, pathlib.Path)


def test_not_using_os_module():
    assert 'os' not in dir()


def test_uniques():
    fi = FolderIterator()
    assert isinstance(fi.uniques, list)


def test_duplicates():
    fi = FolderIterator()
    assert isinstance(fi.duplicates, dict)


def test_find_unique_vals():
    fi = FolderIterator()
    fi.iter_folder()
    vals_to_find = ['d', 'j', 'q', 'o', 'b', 't', 'f', 'v', 'c', 'l', 'a', 'z', 'r', 'y', 'e', 'w', 'h', 'g']
    for item in fi.uniques:
        ###
        #print(filename)
        ###
        for val in vals_to_find:
            ### item to filename
            if val in item:
                vals_to_find.remove(val)
                break
    assert vals_to_find == []


def test_unique_keys():
    fi = FolderIterator()
    fi.iter_folder()
    keys = ['S2.2lL',
            'AQ.n5x',
            'rH.rbh',
            'iz.9P3',
            'jG.Roh',
            'kZ.kJo',
            'RZ.9zx',
            'DC.bQx',
            'YO.doV',
            'GZ.pVN',
            '9f.zif',
            'mU.4yL',
            'pd.k0I',
            'Rx.Pe7',
            'rj.PRj',
            '8D.blN',
            'jG.d2t',
            'kI.wOE']
    for key in fi.duplicates:
        for key_to_find in keys:
            if key_to_find in key:
                break
        else:
            assert False

    assert True


if __name__ == "__main__":
    test_functions = ["test_using_pathlib", "test_not_using_os_module", "test_uniques", "test_duplicates", "test_find_unique_vals", "test_unique_keys"]
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