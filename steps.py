from typing import Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar("T")

class Step(Generic[T], ABC):
    @property
    def name(self) -> str:
        """Name of the step"""
        raise NotImplementedError
    def __call__(self, frame: T) -> T:
        return self.process(frame)

    @abstractmethod
    def process(self, frame: T) -> T:
        """Process the frame and return the result"""
        raise NotImplementedError

class NormalizeSpaceStep(Step[T]):
    def process(self, frame: T) -> T:
        if isinstance(frame.data, str):
            return frame.data.strip()
        return frame.data
class TagStep(Step[T]):
    def __init__(self, tag: str) -> None:
        self.tag = tag
    def process(self, frame: T) -> T:
        if frame.meta is None:
            frame.meta["tags"] = []
        frame.meta.append(self.tag)
        return frame
class LenMetaStep(Step[T]):
    def process(self, frame: T) -> T:
        if frame.meta is not None:
            return len(frame.meta)
        return frame