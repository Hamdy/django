from typing import IO, Any
from django.core.files.base import File
from django.core.files.storage import Storage

class FileBackend(Storage):
    def _save(self, name: str | None, content: IO[Any], max_length: int | None = ...) -> str:
        ...
    def _open(self, name: str, mode: str) -> File:
        return super().open(name, mode)
    
    def delete(self, name: str) -> None:
        return super().delete(name)
    def listdir(self, path: str) -> tuple[list[str], list[str]]:
        return super().listdir(path)
    ...
    ...
    