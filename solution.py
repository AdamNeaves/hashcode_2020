import library
import reader
import writer

days_left, remaining_libs = reader.read('./inputs/a_example.txt')
outputs = []
while days_left > 0:
    while len(remaining_libs) > 0:
        next_lib = sorted(remaining_libs, key=lambda x: x.book_score_remaining(days_left))[0]
        remaining_libs.remove(next_lib)
        next_lib.books = next_lib.avail_books()

        for l in remaining_libs:
            l.remove_dupes(next_lib.books.keys())

        days_left = days_left - next_lib.signup
        outputs.append(next_lib)
    writer.write(outputs)
