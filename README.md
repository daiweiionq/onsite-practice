# circuit-utils

A toy quantum circuit helper library, built as the capstone for the onsite training.

## Install (dev)

```bash
uv sync
```

## Run tests / lint / typecheck

```bash
uv run pytest
uv run ruff check .
uv run ty check src/
```

## Usage

```python
from circuit_utils import Gate, Circuit

c = Circuit(num_qubits=2, name='bell')
c.add_gate(Gate('H', [0]))
c.add_gate(Gate('CNOT', [0, 1]))
print(c.depth(), c.gate_names())
```
