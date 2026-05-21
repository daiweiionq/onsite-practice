import json
import logging

from circuit_utils.circuit import Circuit
from circuit_utils.gates import Gate

logger = logging.getLogger(__name__)


def parse_circuit_json(payload: str) -> Circuit:
    """Parse a JSON payload into a Circuit.

    The payload must have ``num_qubits`` and a list of ``gates``; ``name`` is
    optional. Each gate must have ``name`` and ``qubits``; ``angle`` is optional.

    >>> c = parse_circuit_json('{"num_qubits": 2, "name": "bell", '
    ...                   '"gates": [{"name": "H", "qubits": [0]}, '
    ...                   '{"name": "CNOT", "qubits": [0, 1]}]}')
    >>> c.depth()
    2
    >>> c.gate_names()
    ['H', 'CNOT']
    """
    try:
        data = json.loads(payload)
    except json.JSONDecodeError as e:
        raise ValueError(f'Invalid JSON: {e}') from e

    if not isinstance(data, dict):
        raise ValueError(f'Expected JSON object, got {type(data).__name__}')
    if 'num_qubits' not in data:
        raise ValueError("Missing required key 'num_qubits'")

    circuit = Circuit(
        num_qubits=data['num_qubits'],
        name=data.get('name', 'unnamed'),
    )
    for spec in data.get('gates', []):
        circuit.add_gate(Gate(
            name=spec['name'],
            qubits=spec['qubits'],
            angle=spec.get('angle'),
        ))
    logger.info('Parsed circuit %r with %d gates', circuit.name, circuit.depth())
    return circuit
