from .Interface import IngestorInterface
from .QuoteEngine import QuoteModel
from .IngestorEngine import DocxIngestor, CSVIngestor
from typing import List


class Ingestor(IngestorInterface):
    ingestors = [DocxIngestor, CSVIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception(f'Cannot ingest {path}')
        quotes = []
