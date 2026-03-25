from __future__ import annotations


class ApplicationError(Exception):
    def __init__(self, code: str):
        self.code = code
        super().__init__(code)
