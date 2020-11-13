from limits import ContainerLimits
from mounts import ContainerMounts
from capability import ContainerCapability


class CheckContainer:
    def __init__(self, inspected_container):
        self.limits = ContainerLimits(inspected_container)
        self.mounts = ContainerMounts(inspected_container)
        self.capabilities = ContainerCapability(inspected_container)
        self.check_result = dict()

    def check_limits(self):
        ulimit = self.limits.is_ulimits_exists()
        memory = self.limits.is_memory_limits_exists()
        cpu = self.limits.is_cpu_limits_exists()
        pids = self.limits.is_process_limits_exists()
        if not ulimit:
            self.check_result.update({'Ulimit': 'No Ulimits'})
        if not memory:
            self.check_result.update({'Memory': 'No Memory Limits'})
        if not cpu:
            self.check_result.update({'CPU': 'No CPU Limits'})
        if not pids:
            self.check_result.update({'PIDs': 'No PiDs Limits'})
        return self.check_result

    def check_mounts(self):
        not_ro_mounts = self.mounts.get_not_read_only_mounts()
        if not_ro_mounts:
            self.check_result.update({'Mounts': not_ro_mounts})
        return self.check_result

    def check_capability(self):
        drop = self.capabilities.is_cap_drop()
        if not drop:
            self.check_result.update({'CapDrop': 'No dropped capabilities'})

    def check_container(self):
        self.check_limits()
        self.check_mounts()
        self.check_capability()
        return self.check_result
