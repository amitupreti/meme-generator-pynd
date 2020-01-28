from .Interface import IngestorInterface
from .QuoteEngine import QuoteModel

from typing import List
import docx
import pandas as pd


class DocxIngestor(IngestorInterface):
    allowed_extension = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest {path}')
        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != '':
                parsed = para.text.split('-')
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)
        return quotes


class CSVIngestor(IngestorInterface):
    allowed_extension = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest {path}')
        quotes = []
        df = pd.read_csv(path)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)
        return quotes


class TXTIngestor(IngestorInterface):
    allowed_extension = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest {path}')
        quotes = []
        with open(path, 'r') as f:
            data = f.read().splitlines()

        for index, row in data.iterrows():
            parsed = row.split('-')
            new_quote = QuoteModel(parsed[0], parsed[1])
            quotes.append(new_quote)
        return quotes
