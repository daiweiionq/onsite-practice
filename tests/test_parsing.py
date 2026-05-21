import json
import math

import pytest

from circuit_utils import parse_circuit_json


def test_parse_basic_bell():
    payload = json.dumps({
        'num_qubits': 2,
        'name': 'bell',
        'gates': [
            {'name': 'H', 'qubits': [0]},
            {'name': 'CNOT', 'qubits': [0, 1]},
        ],
    })
    c = parse_circuit_json(payload)
    assert c.num_qubits == 2
    assert c.name == 'bell'
    assert c.gate_names() == ['H', 'CNOT']


def test_parse_with_angle():
    payload = json.dumps({
        'num_qubits': 1,
        'gates': [{'name': 'Rx', 'qubits': [0], 'angle': math.pi / 2}],
    })
    c = parse_circuit_json(payload)
    assert c.name == 'unnamed'
    assert c.parametric_gates()[0].angle == pytest.approx(math.pi / 2)


def test_parse_invalid_json_raises():
    with pytest.raises(ValueError, match='Invalid JSON'):
        parse_circuit_json('not json')


def test_parse_missing_num_qubits():
    with pytest.raises(ValueError, match='num_qubits'):
        parse_circuit_json(json.dumps({'gates': []}))


@pytest.mark.slow
def test_parse_large_circuit():
    gates = [{'name': 'H', 'qubits': [i % 4]} for i in range(1000)]
    payload = json.dumps({'num_qubits': 4, 'gates': gates})
    c = parse_circuit_json(payload)
    assert c.depth() == 1000
