from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_vector, plot_histogram
from numpy import pi
import matplotlib.pyplot as plt




# 6 qubits: 0–2 for logical qubit, 3–4 for Bell pair, 5 for teleport destination
# 2 classical bits: for measurement results
qc = QuantumCircuit(5, 2)

### 1. ENCODE LOGICAL QUBIT (3-QUBIT REPETITION CODE)
# Prepare |+> = H|0> on qubit 0
qc.h(0)
# Encode to |+++> → (|000> + |111>)/√2
qc.cx(0, 1)
qc.cx(0, 2)

### 2. CREATE BELL PAIR BETWEEN Q3 (Alice) AND Q4 (Bob)
qc.h(3)
qc.cx(3, 4)

### 3. BELL MEASUREMENT (Teleport the *first* encoded qubit to Q5)
# We'll use qubit 0 from the logical block for the Bell measurement.
# CNOT and H for teleportation protocol
qc.cx(0, 3)
qc.h(0)

# Measure qubits 0 and 3 (these act like "Alice's side")
qc.measure(0, 0)
qc.measure(3, 1)

### 4. CLASSICAL CORRECTION on Bob's qubit (qubit 4)
# Based on classical bits 0 and 1
qc.cx(1, 4)
qc.cz(0, 4)

### 5. MEASURE BOB'S QUBIT (Q5)
qc.draw('mpl')
plt.show()