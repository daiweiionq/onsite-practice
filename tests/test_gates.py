import math

import pytest

from circuit_utils import Gate


def test_gate_not_parametric(hadamard):
    assert not hadamard.is_parametric()


def test_gate_is_parametric(rx_gate):
    assert rx_gate.is_parametric()


def test_gate_angle_normalized():
    g = Gate('Rx', [0], angle=3 * math.pi)
    assert g.angle == pytest.approx(math.pi)


def test_gate_requires_qubits():
    with pytest.raises(ValueError, match='at least one qubit'):
        Gate('H', [])


@pytest.mark.parametrize('name,qubits,is_param', [
    ('H', [0], False),
    ('CNOT', [0, 1], False),
    ('Rx', [0], True),
    ('Rz', [1], True),
])
def test_gate_parametric_table(name, qubits, is_param):
    angle = math.pi / 4 if is_param else None
    g = Gate(name, qubits, angle=angle)
    assert g.is_parametric() == is_param
