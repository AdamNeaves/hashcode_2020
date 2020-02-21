WEIGHTS = {
    "score_remaining": 0,
    "signup_time": -1,  # the lower, the better, hence negative
    # "num_books": 1
    "books_per_day": 0,
    # "average_book_score": 1
}

class Library:

    def __init__(self, idx, books, signup, books_per_day):
        self.idx = idx
        self.books = dict(sorted(books.items(), key=lambda x: -x[1]))
        self.signup = signup
        self.books_per_day = books_per_day
        # print("lib {} created".format(idx))
        # print("lib books: {}".format(self.books))

    def remove_dupes(self, other_books):
        for book in other_books:
            try:
                del self.books[book]
            except KeyError:
                pass

    def calc_total_score(self, books):
        return sum(books.values())

    def avail_books(self, remaining_days):
        days_after_signup = remaining_days - self.signup
        return_dict = {}
        if days_after_signup > 0:
            num_books = self.books_per_day * days_after_signup
            if num_books > len(self.books):
                return_dict =  self.books
            else:
                for x in list(self.books)[:num_books]:
                    return_dict[x] = self.books[x]
                return return_dict
        return return_dict

    def book_score_remaining(self, remaining_days):
        remaining_books = self.avail_books(remaining_days)
        if remaining_books:
            score = sum(remaining_books.values())
        else:
            score = 0
        # print("LIB {} SCORE REMAINING: {}".format(self.idx, score))
        return score

    def get_score(self, remaining_days):
        """score could be based off:
           -amount of time to sign up
           -num books
           -avg score of books
           -books per day
           -num unique books (hard to calculate)
        not 100% sure how to weight them"""
        results = [
            self.book_score_remaining(remaining_days)    * WEIGHTS.get("score_remaining", 0),
            self.signup                                  * WEIGHTS.get("signup_time", 0),
            len(self.avail_books(remaining_days))        * WEIGHTS.get('num_books', 0),
            self.books_per_day                           * WEIGHTS.get('books_per_day', 0),
            (sum(self.books.values()) / len(self.books)) * WEIGHTS.get("average_book_score", 0)
        ]

        return sum(results)

    def books_chonked(self, remaining_days):
        return (remaining_days - self.signup) * self.books_per_day
