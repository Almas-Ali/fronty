__version__ = '0.0.3'

class Fronty:
    def __init__(self, file_path: str) -> None:
        self.__file_path = file_path

    def run(self, debug: bool = True, host: str = '127.0.0.1', port: int = 8000) -> None:
        pass
