from classes import Thing


class Player(Thing):
    def __init__(self, json_path: str) -> None:
        super().__init__(json_path)
        