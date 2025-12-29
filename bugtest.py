
file_path_register_coaches = "coaches_acc.txt"

with open(file_path_register_coaches, 'r') as f:
    for line in f.readlines():
        data = line.strip().split(" | ")
        print(data[0])
        print(data[1])
