import random 

def show(cells):
    board = """
     %s | %s | %s
    -----------
     %s | %s | %s
    -----------
     %s | %s | %s
        
    """ % tuple(cells)

    print(board)


def available_cells(cells):
    indexes = []

    index = 0
    for cell in cells:
        if cell == ' ':
            indexes.append(index)
        index += 1

    return indexes


cells = [' '] * 9
 
while True:
    show(cells)
    print(cells)

    if cells.count(' ') == 0:
        break

    position = int(input("Enter position: " ))

    if position > len(cells):
        print("Invalid index. skipping turn")
    else: 
        cells[position] = 'X'

    cpu_choices = available_cells(cells)
    cpu = random.choice(cpu_choices)
    cells[cpu] = 'O'

