from pyhtml import *

def ren():
    t = html(
        head(
            title("Hello")
        ),
        body(
            h1("World")
        )
    )
    return t.render()
