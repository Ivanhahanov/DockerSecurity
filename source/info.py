def show_info(**kwargs):
    info = get_info(**kwargs)
    for name, text in info.items():
        print(f'- {name}: {text}')


def get_info(**kwargs):
    info = dict()
    for arg in kwargs.keys():
        if arg == 'CapDrop':
            info["Capabilities"] = get_help('capability_help')
        if arg == 'Mounts':
            info["Mounts"] = get_help('mount_help')
        if arg == 'Mounts':
            info["Users"] = get_help('users_help')

    return info


def get_help(filename):
    with open('help/' + filename, 'r') as f:
        return f.read()
