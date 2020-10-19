from abc import ABC, abstractmethod


class Base(ABC):
    """Abstract class don't instantiate the class"""

    @abstractmethod
    def create(self):
        raise AttributeError("you can't use the abstract method")
