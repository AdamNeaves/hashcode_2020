import library
import reader

days_left, remaining_libs = reader.read('./inputs/a_example.txt')
outputs = []
while days_left > 0:
    next_lib = sorted(remaining_libs, key=lambda x: x.book_score_remaining(days_left))[1]
    remaining_libs.remove(next_lib)
    remove_dupes(remaining_libs, next_lib)
    days_left = days_left - next_lib.slider
    outputs.append
    pass


def remove_dupes(remaining_libs, next_lib):
    for l in remaining_libs:
        l.remove_dupes(next_lib.books.keys())
