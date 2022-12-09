from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = next(filter(lambda h: h.name == hardware_name, System._hardware))
        except StopIteration:
            return "Hardware does not exist"
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = next(filter(lambda h: h.name == hardware_name, System._hardware))
        except StopIteration:
            return "Hardware does not exist"
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = next(filter(lambda h: h.name == hardware_name, System._hardware))
        except StopIteration:
            return "Some of the components do not exist"

        try:
            software = next(filter(lambda s: s.name == software_name, System._software))
        except StopIteration:
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        result = ["System Analysis",
                  f"Hardware Components: {len(System._hardware)}",
                  f"Software Components: {len(System._software)}",
                  f"Total Operational Memory: {sum([x.memory_consumption for x in System._software])} / "
                  f"{sum([x.memory for x in System._hardware])}",
                  f"Total Capacity Taken: {sum([x.capacity_consumption for x in System._software])} / "
                  f"{sum([x.capacity for x in System._hardware])}"]
        return "\n".join(result)

    @staticmethod
    def system_split():
        result = []
        for hardware in System._hardware:
            result.extend([f"Hardware Component - {hardware.name}",
                           f"Express Software Components: "
                           f"{len([x for x in hardware.software_components if x.software_type == 'Express'])}",
                           f"Light Software Components: "
                           f"{len([x for x in hardware.software_components if x.software_type == 'Light'])}",
                           f"Memory Usage: "
                           f"{sum([x.memory_consumption for x in hardware.software_components])} / {hardware.memory}",
                           f"Capacity Usage: "
                           f"{sum([x.capacity_consumption for x in hardware.software_components])} / {hardware.capacity}",
                           f"Type: {hardware.hardware_type}",
                           f"Software Components: "
                           f"{'None' if not hardware.software_components else ', '.join([x.name for x in hardware.software_components])}"])

        return "\n".join(result)
