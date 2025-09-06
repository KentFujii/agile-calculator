import abc
from typing import Sequence

from agile_calculator.records.transformed_record import TransformedRecord


class BaseLoader(abc.ABC):

    @abc.abstractmethod
    def run(self, records: Sequence[TransformedRecord]) -> None:
        raise NotImplementedError
