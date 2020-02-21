import library
import reader
import writer
import scorer
import sys
from multiprocessing.pool import ThreadPool as Pool

files = {'a': 'a_example.txt',
         'b': 'b_read_on.txt',
         'c': 'c_incunabula.txt',
         'd': 'd_tough_choices.txt',
         'e': 'e_so_many_books.txt',
         'f': 'f_libraries_of_the_world.txt'}

for f in sys.argv[1]:
    run_file = files[f]
    days_left, remaining_libs = reader.read('./inputs/' + run_file)
    outputs = []
    while days_left > 0 and len(remaining_libs) > 0:
        # Tuning:
        # For b, c, f: 50 is better than 0
        # For e: 0 is better than 50
        next_lib = max(remaining_libs,
                       key=lambda x: x.get_score(days_left, 50))
        remaining_libs.remove(next_lib)
        next_lib.books = next_lib.avail_books(days_left)
        if not next_lib.books:
            continue
        pool_size = len(remaining_libs)
        for l in remaining_libs:
            l.remove_dupes(next_lib.books.keys())

        days_left = days_left - next_lib.signup
        outputs.append(next_lib)

    writer.write('./outputs/' + run_file, outputs)
    print(scorer.score(run_file))
