"""
Usecase of generator is that I can loop trhough a large amount of data
without storing all of them.
I use generator if i don't care about data before or after something
in iteration.
"""

# example


def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
