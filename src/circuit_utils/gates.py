import logging
import math
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class Gate:
    name: str
    qubits: list[int]
    angle: float | None = None

    def __post_init__(self):
        if not self.qubits:
            raise ValueError('Gate must target at least one qubit')
        if self.angle is not None:
            original = self.angle
            self.angle = self.angle % (2 * math.pi)
            if original != self.angle:
                logger.debug('Normalized angle %s -> %s', original, self.angle)

    def __repr__(self) -> str:
        if self.angle is not None:
            return f'{self.name}({self.angle:.4f}) on q{self.qubits}'
        return f'{self.name} on q{self.qubits}'

    def is_parametric(self) -> bool:
        return self.angle is not None
