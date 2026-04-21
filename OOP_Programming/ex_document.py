from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import override


@dataclass
class Document:
    name: str
    content: str
    metadata: dict


class Storage(ABC):
    @abstractmethod
    def save(self, document: Document) -> None:
        ...


class InMemoryStorage(Storage):
    def __init__(self):
        self._documents: list[Document] = []

    @override
    def save(self, document: Document) -> None:
        self._documents.append(document)

    def list_documents(self) -> list[Document]:
        return self._documents.copy()


class Logger:
    @staticmethod
    def info(message: str):
        print(f'[INFO]{message}')

    @staticmethod
    def error(message: str):
        print(f'[ERROR]{message}')


class DocumentProcessor(ABC):
    def _init__(self, storage: Storage, logger: Logger):
        self.storage = storage
        self.logger = logger

    @abstractmethod
    def validate(self, raw_data: str) -> bool:
        ...

    @abstractmethod
    def parse(self, path: Path, raw_data: str) -> Document:
        ...

    @staticmethod
    def enrich(document: Document) -> None:
        document.metadata['Processed'] = True

    def process(self, path: Path, raw_data: str) -> Document:
        self.logger.info(message=f'Start processing: {path.name}')

        if not self.validate(raw_data):
            self.logger.error(message=f'Validation failed for: {path.name}')

            raise ValueError(f'Invalid input for file: {path.name}')

        document = self.parse(path, raw_data)
        self.enrich(document)

        self.storage.save(document)

        self.logger.info(f'Finished processing: {path.name}')

        return document


class CsvProcessor(DocumentProcessor):

    @override
    def validate(self, raw_data: str) -> bool:
        return ',' in raw_data and '\n' in raw_data

    @override
    def parse(self, path: Path, raw_data: str) -> Document:
        rows = raw_data.strip().splitlines()

        column_count = len(rows[0].split(",")) if rows else 0

        return Document(

            name=path.name,

            content=f"csv with {len(rows)} rows",

            metadata={

                "type": "csv",

                "source": str(path),

                "rows": len(rows),

                "columns": column_count,

            },

        )
