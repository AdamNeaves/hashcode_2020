class Library:
    
    def __init__(self, idx, books, signup, books_per_day):
        self.idx = idx
        self.books = books
        self.signup = signup
        self.books_per_day = books_per_day

    def remove_dupes(self, other_books):
        self.books = list(set(self.books) - set(other_books))

    def calc_total_score(self):
        total = 0
        for book in self.books:
            total += self.books[book]
        return total