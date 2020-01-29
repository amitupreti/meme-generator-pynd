import random
import os
import requests

from flask import Flask, render_template, abort, request
from .libs.QuoteEngine import Ingestor
from .libs.MemeEngine import MemeEngine

template_dir = os.path.abspath('./templates/')
static_dir = os.path.abspath('./static/')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

meme = MemeEngine('./static/')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    #  quote_files variable
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = ["./_data/photos/dog/", "./_data/photos/batman/"]
    imgs = []
    for image_path in images_path:
        for root, dirs, files in os.walk(image_path):
            imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    r = requests.get(image_url, allow_redirects=True)
    tmp = f'./tmp/{random.randint(0, 100000000)}.png'
    open(tmp, 'wb').write(r.content)

    path = meme.make_meme(tmp, body, author)

    os.remove(tmp)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
