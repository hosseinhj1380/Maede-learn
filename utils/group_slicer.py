def list_group(group, size):
    sliced_group = []
    for i in range(0, len(group), size):
        sliced_group.append(group[i:i + size])
    return sliced_group
