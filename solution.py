import reader
import writer
import scorer
import sys
from multiprocessing.pool import ThreadPool as Pool
import numpy as np


def solve(problems):
    files = {'a': 'a_example.txt',
             'b': 'b_read_on.txt',
             'c': 'c_incunabula.txt',
             'd': 'd_tough_choices.txt',
             'e': 'e_so_many_books.txt',
             'f': 'f_libraries_of_the_world.txt'}

    pool = Pool()
    for f in problems:
        run_file = files[f]
        days_left, remaining_libs = reader.read('./inputs/' + run_file)
        outputs = []
        while days_left > 0 and len(remaining_libs) > 0:
            # Tuning:
            # For b, c, f: 50 is better than 0
            # For e: 0 is better than 50
            scores = pool.map(lambda x: x.get_score(days_left),
                              remaining_libs)
            next_lib = remaining_libs[np.argmax(scores)]
            _ = pool.map(lambda x: x.scan_copy(), next_lib.books.values())
            remaining_libs.remove(next_lib)
            next_lib.books = next_lib.avail_books(days_left)
            if not next_lib.books:
                continue
            _ = pool.map(lambda x: x.remove_dupes(next_lib.books.keys()),
                         remaining_libs)

            days_left = days_left - next_lib.signup
            outputs.append(next_lib)

        writer.write('./outputs/' + run_file, outputs)
        return scorer.score(run_file)

if __name__ == '__main__':
    score = solve(sys.argv[1])
    print(score[-1])
