class ContainerLimits:
    def __init__(self, inspected_container):
        self.inspected_container = inspected_container

    def is_memory_limits_exists(self):
        # NOT sure
        # TODO: need to check
        memory_limits = self.inspected_container['HostConfig']['Memory']
        if memory_limits == 0:
            return False
        return memory_limits

    def is_cpu_limits_exists(self):
        # NOT sure
        # TODO: need to check
        cpu_limits = self.inspected_container['HostConfig']['Memory']
        if cpu_limits == 0:
            return False
        return cpu_limits

    def is_process_limits_exists(self):
        pid_limits = self.inspected_container['HostConfig']['PidsLimit']
        if pid_limits is None:
            return False
        return pid_limits

    def is_ulimits_exists(self):
        ulimits = self.inspected_container['HostConfig']['Ulimits']
        if ulimits is None:
            return False
        return ulimits