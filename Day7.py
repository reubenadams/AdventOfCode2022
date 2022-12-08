with open('Day7Data.txt', 'r') as f:
    commands = f.read().split('$')
    commands = [cmd.split('\n')[:-1] for cmd in commands[1:-1]] + [commands[-1].split('\n')]
    commands = [[tuple(thing.split()) for thing in cmd] for cmd in commands]


parent_dict_dirs = {}
parent_dict_files = {}
children_dict = {}


cd = '/'
for cmd_result in commands:
    cmd, result = cmd_result[0], cmd_result[1:]  # cmd is cd or ls, result is [] if cd or dir-file list if ls
    if cmd[0] == 'ls':
        children_dict[cd] = result
        for res in result:
            if res[0] == 'dir':
                parent_dict_dirs[res[1]] = cd
            else:
                parent_dict_files[res] = cd
    elif cmd[0] == 'cd':
        new_dir = cmd[1]
        if new_dir == '..':
            cd = parent_dict_dirs[cd]
        else:
            cd = new_dir
    else:
        print('Whoopsie! cmd should be either cd or ls but instead is', cmd[0])


for key in children_dict:
    print(key)
    print('\t', children_dict[key])


print(parent_dict_dirs)
for file in parent_dict_files:
    print(file, parent_dict_files[file])
    

def size(dir, children_dict):
    print('Calculating size')
    print(dir)
    if dir[0] != 'dir':  # i.e. it's not actually a directory but rather a file
        return int(dir[0])
    total = 0
    for thing in children_dict[dir]:
        if thing[0] != 'dir':
            total += int(thing[0])
        else:
            total += size(thing, children_dict)

print(size('/', children_dict))