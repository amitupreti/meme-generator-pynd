import argparse
import os
import random

# @TODO Import your Ingestor and MemeEngine classes
from libs.MemeEngine import MemeEngine
from libs.QuoteEngine import Ingestor, QuoteModel


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/batman/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp/')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = argparse.ArgumentParser(description="Generate your own MEME")
    parser.add_argument('--body', type=str, default=None, help='The quote that you want to add to your MEME')
    parser.add_argument('--author', type=str,
                        default=None, help="The author of the MEME")
    parser.add_argument('--path', type=str,
                        default=None, help="Image path for your MEME")

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
