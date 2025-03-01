

class Rover:
    def __init__(self, pos_x, pos_y, direction):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction = direction.upper()

    def move(self, maxX, maxY):
        if self.direction == 'N':
            self.pos_y += 1
        if self.direction == 'S':
            self.pos_y -= 1

        if self.direction == 'E':
            self.pos_x += 1
        if self.direction == 'W':
            self.pos_x -= 1

        self.fix_position_XY(maxX, maxY)

    # Do not allow the rover get out of the rectangular
    def fix_position_XY(self, maxX, maxY):
        if self.pos_x > maxX:
            self.pos_x = maxX

        if self.pos_y > maxY:
            self.pos_y = maxY

        if self.pos_y < 0:
            self.pos_y = 0

        if self.pos_x < 0:
            self.pos_x = 0

    # Turn to another a new direction
    def turn_to(self, direction):
        key = f"{self.direction}{direction.upper()}"
        options = {
            'NL':'W',
            'SR':'W',
            'NR':'E',
            'SL':'E',
            'WR':'N',
            'EL':'N',
            'ER':'S',
            'WL':'S',
        }

        new_direction = options[key]
        self.direction = new_direction

    # Handle which kind of command is. Is it a Move or "turnTo" command?
    def handle_command(self, command, maxX, maxY):
        command = command.upper()
        if command == 'M':
            self.move(maxX, maxY)

        if command in ['L', 'R']:
            self.turn_to(command)

    def current_position(self):
        return f"{self.pos_x} {self.pos_y} {self.direction}"
