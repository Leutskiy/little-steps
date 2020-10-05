from abc import ABC, abstractmethod


class ISerializer(ABC):
    @abstractmethod
    def serialize(self, object: object) -> str:
        pass
