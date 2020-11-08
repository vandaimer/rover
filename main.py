from rover import Rover


def main():
    print('Enter the grid size. Example: 5 5')
    grid = input().split(' ')

    print('Enter the initial position of the first rover. Example: 1 2 N')
    first_rover_input = input().split(' ')

    print('Enter the commands for the first rover. Example: LMLMLMLMM')
    commands_first_rover = input()

    print('Enter the initial position of the second rover. Example: 3 3 E')
    second_rover_input = input().split(' ')

    print('Enter the commands for the second rover. Example: MMRMMRMRRM')
    commands_second_rover = input()

    MAX_X = int(grid[0])
    MAX_Y = int(grid[1])
    commands = []

    first_rover = Rover(int(first_rover_input[0]), int(first_rover_input[1]), first_rover_input[2])
    second_rover = Rover(int(second_rover_input[0]), int(second_rover_input[1]), second_rover_input[2])

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
