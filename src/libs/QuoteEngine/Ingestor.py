from .Interface import IngestorInterface
from .QuoteEngine import QuoteModel
from .IngestorEngine import DocxIngestor, CSVIngestor, TextIngestor, PDFIngestor
from typing import List


class Ingestor(IngestorInterface):
    """Main Ingestor that can automatically parse the supported file types"""
    ingestors = [DocxIngestor, CSVIngestor, TextIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parses the given file if it is supported and Returns the QuoteModel Object.
        :param path: path to file
        :return: QuoteModel object
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                quotes = ingestor.parse(path)
                return quotes
