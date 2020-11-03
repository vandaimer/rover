from rover import Rover


def main():
    print('Enter the grid size. Example: 5 5')
    grid = input().split(' ')

    print('Enter the initial position of the first rover. Example: 1 2 N')
    first_rover_input = input().split(' ')
    print(first_rover_input)
    print('Enter the commands for the first rover. Example: LMLMLMLMM')
    commands_first_rover = input()
    print(commands_first_rover)

    print('Enter the initial position of the second rover. Example: 3 3 E')
    second_rover_input = input().split(' ')
    print(second_rover_input)
    print('Enter the commands for the second rover. Example: MMRMMRMRRM')
    commands_second_rover = input()
    print(commands_second_rover)

    MAX_Y = grid[0]
    MAX_X = grid[1]
    commands = []

    first_rover = Rover(first_rover_input[0], first_rover_input[1], first_rover_input[2])
    second_rover = Rover(second_rover_input[0], second_rover_input[1], second_rover_input[2])

    commands[:] = commands_first_rover

    for command in commands:
        first_rover.handle_command(command, MAX_X, MAX_Y)

    commands[:] = commands_second_rover

    for command in commands:
        second_rover.handle_command(command, MAX_X, MAX_Y)

    print(first_rover.current_position())
    print(second_rover.current_position())



if __name__ == "__main__":
    main();
