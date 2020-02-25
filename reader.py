from library import Library, Book


def read(file_name):
    with open(file_name, 'r') as f:
        line = f.readline()
        num_books, num_libs, num_days = [int(l) for l in line.split()]
        line = f.readline()
        books = {i: Book(i, int(v)) for i, v in enumerate(line.split())}
        libs = []
        for i in range(num_libs):
            line = f.readline()
            nb, su, bpd = [int(l) for l in line.split()]
            line = f.readline()
            book_ids = [int(l) for l in line.split()]
            lb = {j: books[j] for j in book_ids}
            for b in lb.values():
                b.register_copy()
            libs.append(Library(i, lb, su, bpd))

    return num_days, libs
