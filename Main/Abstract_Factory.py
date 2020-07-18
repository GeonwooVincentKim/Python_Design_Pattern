class DiagramFactory:
    def make_diagram(self, width, height):
        return Diagram(width, height)


class Text:
    def __init__(self, x, y, text, fontsize):
        self.x = x
        self.y = y
        self.rows = [list(text)]


class Diagram:
    def __init__(self):
        self.diagram = None

    def add(self, component):
        for y, row in enumerate(component.rows):
            for x, char in enumerate(row):
                self.diagram[y + component.y][x + component.x] = char
