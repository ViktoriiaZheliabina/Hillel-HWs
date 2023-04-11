# 2.Створити ітератор, що прийме послідовність і буде перебирати значення в заданому діапазоні.
# CustomIterator(sequence, start_index, end_index)

class CustomIterator:
    """Class that accepts a sequence and iterates through the values in the given range"""

    def __init__(self, sequence: list, start_index: int, end_index: int):
        """

        :param sequence: a sequence to iterate
        :param start_index: start index
        :param end_index: end index
        """
        if start_index < 0 or start_index >= len(sequence):
            raise BaseException("start index out of range")
        if start_index > end_index:
            raise BaseException("start index is greater than end index")
        if end_index < 0 or end_index >= len(sequence):
            raise BaseException("end index out of range")
        self.sequence = sequence
        self.end_index = end_index
        self.position = start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.position <= self.end_index:
            item = self.sequence[self.position]
            self.position += 1
            return item
        else:
            raise StopIteration
