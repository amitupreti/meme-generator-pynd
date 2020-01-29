from .Interface import IngestorInterface
from .QuoteEngine import QuoteModel

from typing import List
import os
import subprocess
import random

import pandas as pd
import docx


class DocxIngestor(IngestorInterface):
    """Parses docs files"""
    allowed_extension = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parses the DOCx file and Returns the QuoteModel Object.
        :param path: path to Docx file
        :return: QuoteModel object
        """
        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest {path}')
        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != '':
                parsed = para.text.split('-')
                new_quote = QuoteModel(parsed[0].strip(), parsed[1].strip())
                quotes.append(new_quote)
        return quotes


class CSVIngestor(IngestorInterface):
    """Parses CSV files."""
    allowed_extension = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parses the csv file and Returns the QuoteModel Object.
        :param path: path to csv file
        :return: QuoteModel object
        """
        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest {path}')
        quotes = []
        df = pd.read_csv(path)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)
        return quotes


class TextIngestor(IngestorInterface):
    """Parses txt files."""
    allowed_extension = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parses the text file and Returns the QuoteModel Object.
        :param path: path to text file
        :return: QuoteModel object
        """
        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest {path}')
        quotes = []
        with open(path, 'r') as f:
            data = f.read().strip().splitlines()

        for row in data:
            if row:
                parsed = row.split('-')
                new_quote = QuoteModel(parsed[0].strip(), parsed[1].strip())
                quotes.append(new_quote)
        return quotes


class PDFIngestor(IngestorInterface):
    """Parses PDF files."""
    allowed_extension = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parses the PDF file and Returns the QuoteModel Object.
       :param path: path to PDF file
       :return: QuoteModel object
       """
        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest {path}')
        quotes = []
        temp_file = f'./tmp/{random.randint(0, 1000000)}quotes.txt'
        call = subprocess.call(['pdftotext', path, temp_file])

        # a binary line in the pdf is causing error while reading
        with open(temp_file, 'r', encoding="utf8") as f:
            data = f.read().strip().splitlines()
            for row in data:
                row = row.strip()
                if row:
                    parsed = row.split('-')
                    new_quote = QuoteModel(parsed[0].strip(), parsed[1].strip())
                    quotes.append(new_quote)

        os.remove(temp_file)
        return quotes
