import logging
from dataclasses import dataclass, field

from circuit_utils.gates import Gate

logger = logging.getLogger(__name__)


@dataclass
class Circuit:
    num_qubits: int
    name: str = 'unnamed'
    gates: list[Gate] = field(default_factory=list)

    def __post_init__(self):
        if self.num_qubits < 1:
            raise ValueError(f'Circuit needs at least 1 qubit, got {self.num_qubits}')
        logger.info('Circuit %r created: %d qubits', self.name, self.num_qubits)

    def add_gate(self, gate: Gate) -> None:
        for q in gate.qubits:
            if q >= self.num_qubits:
                raise ValueError(
                    f'Qubit {q} out of range for {self.num_qubits}-qubit circuit'
                )
        self.gates.append(gate)
        logger.debug('Added gate %r, depth now %d', gate, self.depth())

    def depth(self) -> int:
        return len(self.gates)

    def gate_names(self) -> list[str]:
        return [g.name for g in self.gates]

    def parametric_gates(self) -> list[Gate]:
        return [g for g in self.gates if g.is_parametric()]
