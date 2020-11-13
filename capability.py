class ContainerCapability:
    def __init__(self, inspected_container):
        self.inspected_container = inspected_container

    def is_cap_drop(self):
        dropped_cap = self.inspected_container['HostConfig'].get('CapDrop', None)
        if dropped_cap is None:
            return False
        if type(dropped_cap) is list:
            if dropped_cap == ['ALL']:
                return True

    def is_cap_add(self):
        added_cap = self.inspected_container['HostConfig'].get('CapAdd', None)
        if added_cap is None:
            return True
        return added_cap
