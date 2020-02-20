import library
import reader
import writer

files = {'a': 'a_example.txt',
         'b': 'b_read_on.txt',
         'c': 'c_incunabula.txt',
         'd': 'd_tough_choices.txt',
         'e': 'e_so_many_books.txt',
         'f': 'f_libraries_of_the_world.txt'}

run_file = files['d']
days_left, remaining_libs = reader.read('./input/' + run_file)
outputs = []
while days_left > 0 and len(remaining_libs) > 0:
    remaining_libs = sorted(remaining_libs, key=lambda x: x.signup)
    next_lib = remaining_libs[0]
    remaining_libs.remove(next_lib)
    next_lib.books = next_lib.avail_books(days_left)
    if not next_lib.books:
        continue
    for l in remaining_libs:
        l.remove_dupes(next_lib.books.keys())

    days_left = days_left - next_lib.signup
    outputs.append(next_lib)

writer.write('./output/' + run_file, outputs)
