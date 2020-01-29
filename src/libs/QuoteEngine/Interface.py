from abc import ABC, abstractmethod
from typing import List
from .QuoteEngine import QuoteModel


class IngestorInterface(ABC):
    """Base Ingestor Interface to be realised by Various file Ingesters."""
    allowed_extension = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Checks if the file type is supported by our Ingestor."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extension

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract class to parse a file."""
        pass
