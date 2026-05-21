import math

import pytest

from circuit_utils import Circuit, Gate


@pytest.fixture
def hadamard():
    return Gate('H', [0])


@pytest.fixture
def rx_gate():
    return Gate('Rx', [0], angle=math.pi / 2)


@pytest.fixture
def bell_circuit():
    c = Circuit(num_qubits=2, name='bell')
    c.add_gate(Gate('H', [0]))
    c.add_gate(Gate('CNOT', [0, 1]))
    return c
