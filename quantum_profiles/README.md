# Quantum Profiles

This directory contains various quantum processor profiles that Pandora can dynamically select and switch between.

## Available Profiles

### Empire Profile (`'empire'`)

The Empire Quantum Virtual Processor is a hierarchical quantum computing architecture featuring:

- **Central Control Lattice**: A QuantumVirtualProcessor supervised by Pandora (default: 4 qubits, configurable)
- **Kaleidoscopic Hives Grid**: An expandable 2D grid of HiveQuantumVirtualProcessors (default: 2x2 grid, 8 qubits per hive)

#### Features

1. **Dynamic Expansion**: Expand both the control lattice size and the hive grid dimensions at runtime
2. **Flexible Targeting**: Direct quantum operations to:
   - The entire Empire (control + all hives)
   - Just the control lattice
   - Any specific hive block
3. **Full Addon Support**: Register and execute addons to extend functionality
4. **Comprehensive API**: Clean, well-documented interface for all operations

#### Usage

```python
from quantum_profiles import get_profile

# Create Empire processor with default settings
empire = get_profile('empire')

# Create with custom configuration
empire = get_profile('empire', 
                    control_qubits=6, 
                    grid_size=(3, 3), 
                    hive_qubits=12)

# Apply gates to different targets
empire.apply_gate_to_empire("H", 0)           # Entire empire
empire.apply_gate_to_control_lattice("X", 1)  # Control only
empire.apply_gate_to_hive((0, 0), "Y", 2)     # Specific hive

# Perform measurements
results = empire.measure_empire()         # Measure everything
control = empire.measure_control_lattice() # Control only
hive = empire.measure_hive((1, 1))        # Specific hive

# Dynamic expansion
empire.expand_grid((4, 4))              # Expand hive grid
empire.expand_control_lattice(8)        # Expand control lattice

# Addon support
empire.register_addon(my_addon)
result = empire.execute_addon("addon_name")
```

#### Architecture Details

**Control Lattice**:
- Implemented as a `QuantumVirtualProcessor`
- Coordinates and supervises all hive operations
- Configurable qubit count (default: 4)
- Can be expanded dynamically

**Kaleidoscopic Hives**:
- Each hive is a `HiveQuantumVirtualProcessor` 
- Arranged in a 2D grid with (row, col) addressing
- Default configuration: 2x2 grid with 8 qubits per hive
- Grid can be expanded without recreating the Empire

**Total Qubits**: `control_qubits + (grid_rows × grid_cols × hive_qubits)`

#### API Reference

##### EmpireQuantumVirtualProcessor

**Constructor**:
```python
EmpireQuantumVirtualProcessor(control_qubits=4, grid_size=(2,2), hive_qubits=8)
```

**Key Methods**:
- `expand_grid(new_grid_size)` - Expand the hive grid
- `expand_control_lattice(new_qubit_count)` - Expand control lattice
- `apply_gate_to_empire(gate, reg)` - Apply gate to entire empire
- `apply_gate_to_control_lattice(gate, reg)` - Apply gate to control only
- `apply_gate_to_hive(hive_id, gate, reg)` - Apply gate to specific hive
- `measure_empire()` - Measure entire empire
- `measure_control_lattice()` - Measure control only
- `measure_hive(hive_id)` - Measure specific hive
- `get_hive(hive_id)` - Get reference to specific hive
- `list_hives()` - List all hive IDs
- `register_addon(addon)` - Register an addon
- `execute_addon(addon_name, *args, **kwargs)` - Execute addon
- `get_empire_stats()` - Get Empire statistics

##### HiveQuantumVirtualProcessor

**Constructor**:
```python
HiveQuantumVirtualProcessor(qubits=8, hive_id=None)
```

Inherits all methods from `QuantumVirtualProcessor` and adds hive-specific identification.

## Adding New Profiles

To add a new quantum processor profile:

1. Create a new Python file in this directory (e.g., `myprofile_quantum_virtual_processor.py`)
2. Implement your processor class
3. Register it in `__init__.py` by adding to `QUANTUM_PROFILES` dictionary
4. Update this README with documentation

Example:
```python
# In __init__.py
from quantum_profiles.myprofile_quantum_virtual_processor import MyProfileProcessor

QUANTUM_PROFILES = {
    'empire': EmpireQuantumVirtualProcessor,
    'myprofile': MyProfileProcessor,
}
```

## Testing

Run the test suite:
```bash
python3 test_empire_quantum_processor.py
```

Run the demonstration:
```bash
python3 demo_empire_processor.py
```

## Compatibility

All quantum processor profiles should be compatible with:
- The base `QuantumVirtualProcessor` interface
- Pandora's addon system
- Dynamic configuration and runtime modification
