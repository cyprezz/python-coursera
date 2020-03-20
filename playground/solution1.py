import os


class FileReader:
    def __init__(self, filename):
        self._filename = filename
        self._contents = ''

    def read(self):
        try:
            with open(self._filename) as f:
                self._contents = f.read()
        except FileNotFoundError:
            self._contents = ''
        finally:
            return self._contents


if __name__ == "main":
    print('')
