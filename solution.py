import library
import reader
import writer
import sys
import scorer
from itertools import permutations, product

files = {'a': 'a_example.txt',
         'b': 'b_read_on.txt',
         'c': 'c_incunabula.txt',
         'd': 'd_tough_choices.txt',
         'e': 'e_so_many_books.txt',
         'f': 'f_libraries_of_the_world.txt'}

class Solution:

    def __init__(self, f):
        self.run_file = files[f]
        self.days_left, self.remaining_libs = reader.read('./inputs/' + self.run_file)

    def run(self):
        outputs = []
        while self.days_left > 0 and len(self.remaining_libs) > 0:
            # Tuning:
            # For b, c, f: 50 is better than 0
            # For e: 0 is better than 50
            next_lib = max(self.remaining_libs,
                       key=lambda x: self.get_lib_score(x))
            print("Signup Lib {} with score of {}".format(next_lib.idx, next_lib.get_score(self.days_left)))
            try:
                self.remaining_libs.remove(next_lib)
            except ValueError:
                continue
            next_lib.books = next_lib.avail_books(self.days_left)
            if not next_lib.books:
                continue
            for l in self.remaining_libs:
                l.remove_dupes(next_lib.books.keys())

            self.days_left = self.days_left - next_lib.signup
            outputs.append(next_lib)

        writer.write('./outputs/' + self.run_file, outputs)

    def get_lib_score(self, lib):
        if lib.book_score_remaining(self.days_left):
            return lib.get_score(self.days_left)
        else:
            self.remaining_libs.remove(lib)
            return 0

if __name__ == "__main__":
    inputs = sys.argv[1]
    try:
        loop_toggle = sys.argv[2]
    except:
        loop_toggle = None

    for f in inputs:
        options = [0, 1, -1, 0.5, -0.5]
        if loop_toggle:
            perms = list(product(options, repeat=len(library.WEIGHTS)))
            print([perm for perm in perms])
            scores = {}
            for perm in perms:
                library.WEIGHTS = dict((key, val) for key, val in zip(library.WEIGHTS, perm))
                print(library.WEIGHTS)
                solution = Solution(f)
                solution.run()
                score = scorer.score(solution.run_file)
                print("For weights {}".format(library.WEIGHTS))
                print("Score was: {}".format(score))
                insights = scorer.get_insights(solution.run_file)
                avg_score = sum(insights['scanned_books'].values()) / len(insights['scanned_books'])
                num_books = len(insights['scanned_books'])
                print("Average Score:     {}".format(avg_score))
                print("Min Score:         {}".format(min(insights['scanned_books'].values())))
                print("Max Score:         {}".format(max(insights['scanned_books'].values())))
                print("Num books Scanned: {}".format(num_books))
                print("Num Libraries:     {}".format(insights["num_libs"]))
                scores[perm] = {
                    "score": score,
                    "avg": avg_score,
                    "min": min(insights['scanned_books'].values()),
                    "max": max(insights['scanned_books'].values()),
                    "num_books": num_books,
                    "num_lib": insights["num_libs"]
                }
            # print(scores)
            max_scores = max(scores, key=lambda x: scores[x]["score"])
            print("{}: {}".format(max_scores, scores[max_scores]))
        else:
            solution = Solution(f)
            solution.run()
            score = scorer.score(solution.run_file)
            print("For weights {}".format(library.WEIGHTS))
            print("Score was: {}".format(score))
            insights = scorer.get_insights(solution.run_file)
            avg_score = sum(insights['scanned_books'].values()) / len(insights['scanned_books'])
            num_books = len(insights['scanned_books'])
            print("Average Score:     {}".format(avg_score))
            print("Min Score:         {}".format(min(insights['scanned_books'].values())))
            print("Max Score:         {}".format(max(insights['scanned_books'].values())))
            print("Num books Scanned: {}".format(num_books))
            print("Num Libraries:     {}".format(insights["num_libs"]))
