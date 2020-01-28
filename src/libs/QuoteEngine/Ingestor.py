from .Interface import IngestorInterface
from .QuoteEngine import QuoteModel
from .IngestorEngine import DocxIngestor, CSVIngestor, TextIngestor, PDFIngestor
from typing import List


class Ingestor(IngestorInterface):
    ingestors = [DocxIngestor, CSVIngestor, TextIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                quotes = ingestor.parse(path)
                return quotes
