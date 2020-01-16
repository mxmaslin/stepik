k = int(input())

world = [
    ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
    ['#', '#', '#', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]

world_size = len(world)


def get_vicinity_borders(coord):
    start = coord - 1
    stop = coord + 2
    if coord == 0:
        start = 0
    if coord == world_size - 1:
        stop = world_size
    return start, stop


def get_vicinity(start_x, stop_x, start_y, stop_y):
    vicinity = [
        world[x][y] 
        for x in range(start_x, stop_x) 
        for y in range(start_y, stop_y) 
    ]
    return vicinity


def calculate_new_cell(x, y, vicinity):
    cell = world[x][y]
    new_cell = cell
    if cell == '.':
        if vicinity.count('#') == 3:
            new_cell = '#'
    else:
        if vicinity.count('#') - 1 < 2 or vicinity.count('#') - 1 > 3:
            new_cell = '.'         
    return new_cell


def generate_next_world():
    next_world = []
    for x in range(world_size):
        start_x, stop_x = get_vicinity_borders(x)
        next_world.append([])
        for y in range(world_size):
            start_y, stop_y = get_vicinity_borders(y)
            vicinity = get_vicinity(start_x, stop_x, start_y, stop_y)
            new_cell = calculate_new_cell(x, y, vicinity)
            next_world[x].append(new_cell)
    return next_world

for _ in range(k):
    world = generate_next_world()

for row in world:
    print(row)
    