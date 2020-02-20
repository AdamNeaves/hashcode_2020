from .library import Library


def read(file_name):
    with open(file_name, 'r') as f:
        line = f.readline()
        num_books, num_libs, num_days = [int(l) for l in line.split()]
        line = f.readline()
        books = {i: int(v) for i, v in enumerate(line.split())}
        libs = []
        for _ in range(num_libs):
            line = f.readline()
            nb, su, bpd = [int(l) for l in line.split()]
            line = f.readline()
            book_ids = [int(l) for l in line.split()]
            lb = {i: books[i] for i in book_ids}
            libs.append(Library(lb, su, bpd))

    return num_days, libs
