"""

Copyright 2020 Egor Vavilov

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

import math
import turtle

def drawing_polygons(polygons: int, size: int, corners: int, index: int):
    """
    Draws polygons from small to large.

    polygons - quantity of drawn polygons
    size - size of one side
    corners - quantity of corners
    index - enlargement of one side for next polygon
    """
    turtle.shape('turtle')
    turtle.dot(7, 'red')  # The center dot x0 = 0, y0 = 0

    for a in range(0, polygons):
        radius = size / (2 * math.sin(math.radians(180) / corners))
        alpha = 180 * (corners - 2) / corners
        gamma = alpha / 2

        x = - (radius * math.cos(math.radians(gamma)))  # The X-coordinate of left corner for each square
        y = - (radius * math.sin(math.radians(gamma)))  # The Y-coordinate of left corner for each square

        turtle.up()
        turtle.goto(x, y)
        turtle.down()

        for i in range (0, corners):
            turtle.forward(size)
            turtle.left(360 / corners)
        size += index

        turtle.up()
        turtle.goto(x, y)
        turtle.down()

    turtle.done()
