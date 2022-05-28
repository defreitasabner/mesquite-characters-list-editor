import re

class Regex:
    def __init__(self) -> None:
        self.__pattern_character: str = '([0-9]+)[.][ ](.+)'
        self.__pattern_state: str = '([0-9]+)[ ](.+)'

    def match_character(self, text: str):
        return re.match(self.__pattern_character, text)

    def match_state(self, text: str):
        return re.match(self.__pattern_state, text)
