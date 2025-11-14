"""
Quantum Profiles Package
=========================

This package contains various quantum processor profiles that Pandora can
dynamically select and switch between.

Available Profiles:
- 'empire': Empire Quantum Virtual Processor with hierarchical architecture
"""

from quantum_profiles.empire_quantum_virtual_processor import (
    EmpireQuantumVirtualProcessor,
    HiveQuantumVirtualProcessor
)

# Registry of available quantum profiles
QUANTUM_PROFILES = {
    'empire': EmpireQuantumVirtualProcessor
}


def get_profile(profile_name, **kwargs):
    """
    Get a quantum processor profile by name.
    
    Args:
        profile_name (str): Name of the profile to retrieve (e.g., 'empire')
        **kwargs: Configuration parameters for the profile
        
    Returns:
        Instance of the requested quantum processor profile
        
    Raises:
        KeyError: If the profile name is not registered
        
    Example:
        >>> processor = get_profile('empire', control_qubits=6, grid_size=(3, 3))
    """
    if profile_name not in QUANTUM_PROFILES:
        available = ', '.join(QUANTUM_PROFILES.keys())
        raise KeyError(
            f"Profile '{profile_name}' not found. "
            f"Available profiles: {available}"
        )
    
    profile_class = QUANTUM_PROFILES[profile_name]
    return profile_class(**kwargs)


def list_profiles():
    """
    List all available quantum processor profiles.
    
    Returns:
        list: List of available profile names
    """
    return list(QUANTUM_PROFILES.keys())


__all__ = [
    'EmpireQuantumVirtualProcessor',
    'HiveQuantumVirtualProcessor',
    'QUANTUM_PROFILES',
    'get_profile',
    'list_profiles'
]
