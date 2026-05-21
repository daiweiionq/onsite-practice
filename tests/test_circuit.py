import pytest

from circuit_utils import Circuit, Gate


def test_circuit_depth(bell_circuit):
    assert bell_circuit.depth() == 2


def test_circuit_gate_names(bell_circuit):
    assert bell_circuit.gate_names() == ['H', 'CNOT']


def test_circuit_no_parametric_gates(bell_circuit):
    assert bell_circuit.parametric_gates() == []


def test_circuit_qubit_out_of_range(bell_circuit):
    with pytest.raises(ValueError, match='out of range'):
        bell_circuit.add_gate(Gate('H', [99]))


def test_circuit_requires_qubit():
    with pytest.raises(ValueError):
        Circuit(num_qubits=0)
