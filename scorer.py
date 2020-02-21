


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


def read(file_name):
    with open('./inputs/' + file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        books = {i: int(v) for i, v in enumerate(line.split())}

    return books

def get_insights(file_name):
    # need: num libraries signed up, average signup time, num books, average score per book
    with open('./outputs/' + file_name, 'r') as outp:
        all_books = read(file_name)
        scanned_books = books_scanned(file_name)
        book_score_dict = {}
        for book in scanned_books:
            book_score_dict[int(book)] = all_books[int(book)]
        total_score = score(file_name)
        average_score = total_score/len(scanned_books)
        num_libs = int(outp.readline())
    
    return {
        "scanned_books": book_score_dict,
        "num_libs": num_libs
    }