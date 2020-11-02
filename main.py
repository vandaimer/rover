from robot import Robot

def main():
    MAX_Y = 5 - 1
    MAX_X = 5 - 1
    commands = []

    # r = Robot(1, 2, 'N')
    # commands[:] = 'LMLMLMLMM'
    # print('--Starting--', r.current_position())
    # for command in commands:
    #     r.handle_command(command, MAX_X, MAX_Y)
    #     print(r.current_position())

    r = Robot(3, 3, 'E')
    commands[:] = 'MMRMMRMRRM'
    print('--Starting--', r.current_position())
    for command in commands:
        r.handle_command(command, MAX_X, MAX_Y)
        print(r.current_position())


if __name__ == "__main__":
    main();
