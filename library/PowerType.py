from enum import Enum

class PowerType(Enum):
    """Defensive powers must end with _DEF"""
    CUT = 1,
    CUT_DEF = 2,
    SMASH = 3,
    SMASH_DEF = 4,
    VENOM = 5,
    VENOM_DEF = 6