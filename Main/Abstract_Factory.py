SVG_TEXT = """<text x="{x}" y="{y}" text-anchor="left"\
font-family="sans-sefit" font-size"{fontsize}">{text}</text>"""

SVG_RECTANGLE = """<rect x="{x}" y="{y}" width="{width}" \
height="{height}" fill="{fill}" stroke="{stroke}"/>"""

SVG_SCALE = 20
SVG_START = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"
    "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve"
    width="{pxwidth}px" height="{pxheight}px">"""
SVG_END = "</svg>\n"

BLANK = " "
CORNER = "+"
HORIZONTAL = "-"
VERTICAL = "|"


# Use only Diagram Factory as an arguments and Generate the requested Diagram.
def create_diagram(factory):
    diagram = factory.make_diagram(30, 7)
    rectangle = factory.make_rectangle(4, 1, 2, 5, "yellow")
    text = factory.make_text(7, 3, "Abstract Factory")
    diagram.add(rectangle)
    diagram.add(text)
    return diagram


# Abstract Class named DiagramFactory.
class DiagramFactory:
    def make_diagram(self, width, height):
        return Diagram(width, height)

    def make_rectangle(self, x, y, width, height, fill="white", stroke="black"):
        return Rectangle(x, y, width, height, fill, stroke)

    def make_test(self, x, y, text, fontsize=12):
        return Text(x, y, text, fontsize)


class Diagram:
    def __init__(self):
        self.diagram = None

    def add(self, component):
        for y, row in enumerate(component.rows):
            for x, char in enumerate(row):
                self.diagram[y + component.y][x + component.x] = char


class Rectangle:
    def __init__(self, x, y, width, height, fill, stroke):
        self.x = x
        self.y = y
        self.rows = _create_ractangle(
            width, height,
            BLANK if fill == "white" else "%"
        )


class SvgDiagramFactory(DiagramFactory):
    def make_diagram(self, width, height):
        return SvgDiagram(width, height)


class SvgDiagram:
    def __init__(self, width, height):
        pxwidth = width * SVG_SCALE
        pxheight = height * SVG_SCALE
        self.diagram = [SVG_START.format(**locals())]

    def add(self, component):
        self.diagram.append(component.svg)


class SvgRectangle:
    def __init__(self, x, y, width, height, fill, stroke):
        x *= SVG_SCALE
        y *= SVG_SCALE
        width *= SVG_SCALE
        height *= SVG_SCALE
        self.svg = SVG_RECTANGLE.format(**locals())


class Text:
    def __init__(self, x, y, text, fontsize):
        self.x = x
        self.y = y
        self.rows = [list(text)]


class SvgText:
    def __init__(self, x, y, text, fontsize):
        x += SVG_SCALE
        y += SVG_SCALE
        fontsize += SVG_TEXT.format(**locals())
        self.svg = SVG_TEXT.format(**locals())


if __name__ == "__main__":
    txtDiagram = create_diagram(DiagramFactory())
    txtDiagram.save(textFilename)
