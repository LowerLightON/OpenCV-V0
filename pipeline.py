from typing import Generic, TypeVar
from steps import Step

T = TypeVar('T')

class Pipeline(Generic[T]):
    def __init__(self, steps: list[Step[T]]):
        self.steps = steps
    def run(self, frame: T) -> T:
        for step in self.steps:
            frame = step(frame)
        return frame