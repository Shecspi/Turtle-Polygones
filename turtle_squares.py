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

# TODO: Change comments from Russian to English
# TODO: Set quantity of squares which will draw

import turtle

turtle.shape('turtle')

size = 50  # Size of source square

# Координаты левого нижнего угла для каждого из квадратов
# Изменяются для каждого следующего квадрата по формуле index / 2
x = 0
y = 0

# Коэффициент изменения следующего квадрата.
# Размер увеличивается на этот коэффициент.
# Координата левого угла на index / 2.
index = 20

for a in range(0, 10):
    for i in range (0, 4):
        turtle.forward(size)
        turtle.left(90)
    size += index

    x -= index / 2
    y -= index / 2

    turtle.up()
    turtle.goto(x, y)
    turtle.down()

turtle.done()
