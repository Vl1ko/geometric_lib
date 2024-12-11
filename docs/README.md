# Geometric_lib

---

Repository for calculating geometric results of figures

> ⚠️
> Working with @geometric_lib packages, you must strictly follow the requirements for the input data of the functions

Each function gets the necessary variables, then returns the required value

## Supported figures and functions

### Circle

#### Area

Use `area(r)` to calculate the area of a circle

    param r (int): Radius of the circle
    return (float): Area of the circle

```
input: print(area(2))
output: 12,56
```

#### Perimeter

Use `perimeter(r)` to calculate the area of a circle

    param r (int): Radius of the circle
    return (float): Area of the circle

```
input: print(perimeter(4))
output: 25,12
```

### Square

#### Area

Use `area(a)` to calculate the area of a square

    param a (int or float): Radius of the square
    return (int or float): Area of the square

```
input: print(area(2))
output: 4

or

input: print(area(2,5))
output: 4,25
```

#### Perimeter

Use `perimeter(a)` to calculate the area of a square

    param a (int or float): Radius of the square
    return (int or float): Area of the square

```
input: print(perimeter(4))
output: 16

or

input: print(perimeter(2,2))
output: 8,8
```

## Unit-test's

Files `circle.py` and `square.py` includes 6 simple test's.

### `Circle.py` area()

| Input |      Output       |
| :---: | :---------------: |
|   0   |         0         |
|  -0   |         0         |
|  -10  |         0         |
|  -1   |         0         |
|  10   | 314.1592653589793 |
|   1   | 3.141592653589793 |

### `Circle.py` peremiter()

| Input |      Output       |
| :---: | :---------------: |
|   0   |         0         |
|  -0   |         0         |
|  -10  |         0         |
|  -1   |         0         |
|  10   | 62.83185307179586 |
|   1   | 6.283185307179586 |

### `Square.py` area()

| Input | Output |
| :---: | :----: |
|   0   |   0    |
|  -0   |   0    |
|  -10  |   0    |
|  -1   |   0    |
|  10   |  100   |
|   1   |   1    |

### `Square.py` perimeter()

| Input | Output |
| :---: | :----: |
|   0   |   0    |
|  -0   |   0    |
|  -10  |   0    |
|  -1   |   0    |
|  10   |   40   |
|   1   |   4    |
