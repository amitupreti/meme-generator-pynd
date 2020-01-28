from .Interface import IngestorInterface
from .QuoteEngine import QuoteModel
from .IngestorEngine import DocxIngestor, CSVIngestor
from typing import List


class Ingestor(IngestorInterface):
    ingestors = [DocxIngestor, CSVIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                quotes = ingestor.parse(path)
                return quotes

        else:
            raise Exception(f'IngestorEngine is unable to read {path}')
