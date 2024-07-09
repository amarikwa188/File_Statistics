import sys
import time
import re
from tkinter import filedialog
from os import stat


def word_count(lns: list[str]) -> int:
    """
    Calculates the total word count of a text file\n
    :param lns: a string array of file lines\n
    :return: word count of the file
    """
    count: int = 0
    for line in lns:
        count += len(line.split())
    return count


def char_counts(lns: list[str]) -> tuple:
    """
    Calculates the total character counts of a file with and without spaces\n
    :param lns: a string array of file linesn
    :return: a tuple in the format (count without spaces, count with spaces)
    """
    count_no_space, count_with_space = 0, 0
    for line in lns:
        count_with_space += len(line)
        count_no_space += len(line.replace(' ', ''))
    return count_no_space, count_with_space


def avg_line_length(lns: list[str]) -> int:
    """
    Calculates the average word count of the lines in a file\n
    :param lns: a string array of file lines\n
    :return: average line length
    """
    return word_count(lns)//len(lns)


def avg_word_length(lns: list[str]) -> float:
    """
    Calculates the average length of a word in a file\n
    :param lns: a string array of file lines\n
    :return: average word length
    """
    total: int = 0
    for line in lns:
        words: list[str] = line.split()
        total += sum(len(word) for word in words)
    return round(total/word_count(lns), 1)


def filename(pth: str) -> str:
    """
    Parses a file name from a file path\n
    :param pth: file path\n
    :return: file name
    """
    return re.split(r"/", pth)[-1]


if __name__ == '__main__':
    print("Select a raw text file.\n")
    path: str = filedialog.askopenfilename(title="Select a file")
    print(f">{filename(path)}\n")
    time.sleep(1)

    with open(path, 'r') as file:
        try:
            lines: list[str] = [line.strip('\n') for line in file.readlines()]
        except UnicodeDecodeError:
            print("::Invalid file type::")
            sys.exit()

        print("DOCUMENT DATA:\n")
        print(f"Word count: {word_count(lines)}")
        print(f"Characters(no spaces): {char_counts(lines)[0]}")
        print(f"Characters(with spaces): {char_counts(lines)[1]}")
        print(f"Lines: {len(lines)}")
        line_length: int = avg_line_length(lines)
        print(f"Average line length: {line_length} {'words' if line_length != 1 else 'word'}")
        word_length: float = avg_word_length(lines)
        print(f"Average word length: {word_length} {'chars' if word_length != 1.0 else 'char'} per word")

        print()
        time.sleep(0.5)

        print("META DATA:\n")
        print(f"Location: {path}")
        print(f"File size: {stat(path).st_size} bytes")

        creation_time: float = stat(path).st_ctime
        modified_time: float = stat(path).st_mtime
        accessed_time: float = stat(path).st_atime

        print(f"Created: {time.ctime(creation_time)}")
        print(f"Last modified: {time.ctime(modified_time)}")
        print(f"Last accessed: {time.ctime(accessed_time)}")
