import tempfile
import os


class File:
    def __init__(self, filepath):
        filename = os.path.basename(filepath)
        self.path = os.path.join(tempfile.gettempdir(), filename)
        self.filepath = filepath
        self.contents = ''
        self.num_elements = 0
        self.current = 0
        self.elements = None

    def __str__(self):
        return self.filepath

    def __add__(self, obj):
        result_file = 'concatenated.txt'
        result_path = os.path.join(tempfile.gettempdir(), result_file)
        result_contents = self.read() + obj.read()
        with open(result_path, 'w') as f:
            f.write(result_contents)
        return self.__class__(result_path)

    def __new__(cls, *args, **kwargs):
        filename = os.path.basename(args[0])
        path = os.path.join(tempfile.gettempdir(), filename)
        if not os.path.isfile(path):
            with open(path, 'w') as f:
                f.write('')
        return object.__new__(cls)

    def __iter__(self):
        if not self.elements:
            contents = self.read()
            self.elements = contents.split('\n')
            self.num_elements = len(self.elements)
            if self.elements[self.num_elements-1] == '':
                self.num_elements -= 1
        return self

    def __next__(self):
        if self.current > self.num_elements:
            raise StopIteration

        if self.current == self.num_elements and self.elements[self.current] == '':
            raise StopIteration

        result = self.elements[self.current]
        self.current += 1
        return result

    def write(self, contents):
        with open(self.path, 'w') as f:
            f.write(contents)
        self.contents = contents

    def read(self):
        with open(self.path, 'r') as f:
            self.contents = f.read()
            return self.contents

    def get_path(self):
        return self.path


if __name__ == '__main__':
    file = File('/tmp/file1.txt')
    file.write('some text \nnew line\nline three\nline four\n')
    second_file = File('/tmp/file2.txt')
    second_file.write('some text \nnew text line\nline new three\nline new four\n')

    result = file + second_file

    i = 0
    for element in result:
        print('[{}] {}'.format(i, element))
        i += 1
    print(result)

