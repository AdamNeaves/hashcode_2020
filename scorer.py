

def score(file_name):
    all_books = read(file_name)
    scanned_books = books_scanned(file_name)
    total = 0
    for b in scanned_books:
        total += all_books[int(b)]
    return total


def books_scanned(file_name):
    books = []
    with open('./outputs/' + file_name, 'r') as f:
        line = f.readline()
        while line:
            line = f.readline()
            line = f.readline()
            books.extend(line.split())
    return books


def fetch_stats(file_name):
    books = []

    with open('./outputs/' + file_name, 'r') as f:
        line = f.readline()
        libs_signed = []
        while line:
            line = f.readline()
            if len(line.split()) > 0:
                libs_signed.extend(line.split()[0])
            line = f.readline()
            books.extend(line.split())
    return books, libs_signed,


def read(file_name):
    with open('./inputs/' + file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        books = {i: int(v) for i, v in enumerate(line.split())}

    return books


def get_libs(file_name):
    libs = {}
    counter = 0
    with open('./inputs/' + file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        while line:
            line = f.readline()
            if len(line.split()) > 0:
                libs[counter] = int(line.split()[1])
                counter += 1
            line = f.readline()

    return libs


def stats(file_name):
    total_score = score(file_name)
    books_scanned, libs_signed = fetch_stats(file_name)
    books_all = read(file_name)
    average_score = total_score/len(books_scanned)
    min_book, max_book = get_min_max(books_scanned, books_scanned)
    total_signup = 0
    libs = get_libs(file_name)
    for l in libs_signed:
        total_signup += libs[int(l)]

    print(f'Score: {total_score}')
    print(f'{len(books_scanned)}/{len(books_all)} books scanned %{(len(books_scanned)/len(books_all))*100}')
    print(f'Min book: {min_book} | Max book: {max_book} | Avg book: {average_score}')
    print(f'{len(libs_signed)}/{len(libs)} libs signed up %{(len(libs_signed)/len(libs))*100}')
    print(f'Avg lib signup: {total_signup/len(libs_signed)} days')


def get_min_max(books_scanned, books_all):
    min_b = 10000000000000
    max_b = 0
    for b in books_scanned:
        if int(books_all[int(b)]) < min_b:
            min_b = int(books_all[int(b)])
        if int(books_all[int(b)]) > max_b:
            max_b = int(books_all[int(b)])
    return min_b, max_b
