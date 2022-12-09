from project.hardware.hardware import Hardware
import math


class PowerHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, "Power", math.floor(capacity * 0.25), math.floor(memory + memory * 0.75))
