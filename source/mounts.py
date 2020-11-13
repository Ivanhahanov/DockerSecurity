class ContainerMounts:
    def __init__(self, inspected_container):
        self.inspected_container = inspected_container

    def get_not_read_only_mounts(self):
        mounts_ro = self.inspected_container['Mounts']
        not_ro_mounts = []
        for mount in mounts_ro:
            if mount['RW']:
                not_ro_mounts.append(mount['Destination'])
        return not_ro_mounts