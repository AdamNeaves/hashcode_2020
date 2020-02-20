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

    def book_score_remaining(self, remaining_days):
        days_after_signup = remaining_days - self.signup

        if days_after_signup > 0:
            num_books = self.books_per_day * days_after_signup
            if num_books > len(self.books):
                return self.books
            else:
                return_dict = {}
                for x in list(self.books)[:num_books]:
                    return_dict[x] = self.books[x]
                return return_dict
        return 0