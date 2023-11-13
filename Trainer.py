from enum import Enum

class Trainer(Enum):
    DT = 'dt'
    RF = 'rf'
    GBC = 'gbc'
    ET = 'et'
    RBFSVM = 'rbfsvm'