def build_tree(node, data):
    while len(data):
        line = data.pop(0)
        cmd = line.split()
        if cmd[0] == "$":
            if cmd[1] == "cd":
                if cmd[2] == "..":
                    node = node["parent"]
                elif cmd[2] == "/":
                    while node["parent"] is not None:
                        node = node["parent"]
                else:
                    build_tree(node["dirs"][cmd[2]], data)
        elif cmd[0] == "dir":
            node["dirs"][cmd[1]] = {"parent": node, "files": {}, "dirs": {}}
        else:
            node["files"][cmd[1]] = int(cmd[0])


def get_smaller_dirs(node, dirs, max_size):
    size = 0
    for d in node["dirs"].values():
        size += get_smaller_dirs(d, dirs, max_size)
    size += sum(v for k, v in node["files"].items())
    if size <= max_size:
        dirs.append(size)
    return size


data = [line.strip() for line in open("input.txt").readlines()]

root = {"parent": None, "files": {}, "dirs": {}}

build_tree(root, data)

small_dir_sizes = []
size = get_smaller_dirs(root, small_dir_sizes, 100_000)
print(sum(small_dir_sizes))  # 1743217

all_dir_sizes = []
total_size = get_smaller_dirs(root, all_dir_sizes, 999_999_999)
min_dir_size = total_size - (70_000_000 - 30_000_000)
print(sorted([d for d in all_dir_sizes if d > min_dir_size])[0])  # 8319096
