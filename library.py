class Library:

    def __init__(self, idx, books, signup, books_per_day):
        self.idx = idx
        self.books = books
        self.signup = signup
        self.books_per_day = books_per_day

    def remove_dupes(self, other_books):
        for book in other_books:
            try:
                del self.books[book]
            except KeyError:
                pass
        # self.books = list(set(self.books) - set(other_books))

    def calc_total_score(self, books):
        total = 0
        for book in books:
            total += books[book]
        return total

    def avail_books(self, remaining_days):
        days_after_signup = remaining_days - self.signup

        if days_after_signup > 0:
            num_books = self.books_per_day * days_after_signup
            if num_books > len(self.books):
                score = self.calc_total_score(self.books)
                return self.books
            else:
                return_dict = {}
                for x in list(self.books)[:num_books]:
                    return_dict[x] = self.books[x]
                score = self.calc_total_score(return_dict)
                return return_dict
        return {}

    def book_score_remaining(self, remaining_days):
        days_after_signup = remaining_days - self.signup

        if days_after_signup > 0:
            num_books = self.books_per_day * days_after_signup
            if num_books > len(self.books):
                score = self.calc_total_score(self.books)
                return score
            else:
                return_dict = {}
                for x in list(self.books)[:num_books]:
                    return_dict[x] = self.books[x]
                score = self.calc_total_score(return_dict)
                return score
        return 0
