from dataclasses import dataclass


@dataclass
class Pair:
    name: str
    value: int


class HashTable:
    def __init__(self, size=0):
        self.size = size

    def _hash(self, key):
        return hash(key) % self.size
