import argparse
import os
import random

from .libs.MemeEngine import MemeEngine
from .libs.QuoteEngine import Ingestor

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate your own MEME")
    parser.add_argument('--body', type=str, default=None, help='The quote body that you want to add to your MEME')
    parser.add_argument('--author', type=str,
                        default=None, help="The author of the MEME")
    parser.add_argument('--path', type=str,
                        default=None, help="Image path for your MEME")

    args = parser.parse_args()
    quote = args.body
    author = args.author
    image = args.path

    # if image is not passed by user
    if image is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        image = random.choice(imgs)

    # handle missing quotes and author
    if quote is None or author is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']

        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        my_quote = random.choice(quotes)
        if quote is None:
            quote = my_quote.body
        if author is None:
            author = my_quote.author

    meme = MemeEngine('./tmp/')
    my_meme = meme.make_meme(img_path=image, text=quote, author=author)
    print(f'Here is your Meme: {my_meme}')
