from typing import Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar("T")

class Step(Generic[T], ABC):
    @property
    def name(self) -> str:
        """Name of the step"""
        return self.__class__.__name__
    def __call__(self, frame: T) -> T:
        return self.process(frame)

    @abstractmethod
    def process(self, frame: T) -> T:
        """Process the frame and return the result"""
        raise NotImplementedError

class NormalizeSpaceStep(Step[T]):
    def process(self, frame: T) -> T:
        if isinstance(frame.data, str):
            frame.data = " ".join(frame.data.split())
            return frame
        return frame
class TagStep(Step[T]):
    def __init__(self, tag: str) -> None:
        self.tag = tag
    def process(self, frame: T) -> T:
        if "tags" not in frame.meta:
            frame.meta["tags"] = []
        frame.meta["tags"].append(self.tag)
        return frame
class LenMetaStep(Step[T]):
    def process(self, frame: T) -> T:
        try:
            frame.meta["len"] = len(frame.data)
        except TypeError:
            frame.meta["len"] = None
        return frame

