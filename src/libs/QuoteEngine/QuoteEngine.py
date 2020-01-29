class QuoteModel:
    """Quote Model class that creates the default formatting for quotes."""

    def __init__(self, body, author):
        self.body = body
        self.author = author.capitalize()

    def __repr__(self):
        return f'{self.body} - {self.author}'
