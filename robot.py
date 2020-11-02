

class Robot:
    def __init__(self, pos_x, pos_y, direction):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction = direction

    def move(self, maxX, maxY):
        if self.direction == 'N':
            self.pos_y += 1
        if self.direction == 'S':
            self.pos_y -= 1

        if self.direction == 'E':
            self.pos_x += 1
        if self.direction == 'W':
            self.pos_x -= 1

    def turnTo(self, direction):
        key = f"{self.direction}{direction}"
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

    def handle_command(self, command, maxX, maxY):
        if command == 'M':
            self.move(maxX, maxY)

        if command in ['L', 'R']:
            self.turnTo(command)

    def current_position(self):
        return f"{self.pos_x} {self.pos_y} {self.direction}"
