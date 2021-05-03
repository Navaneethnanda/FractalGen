# Fractalgen
Fractal-gen is a open library which can be used to generate, experiment and create fractal images using IFS'. IFS' are Iterated Function Systems which are used in one of the methods in constructing fractals. IFS' are simply set of Affine equations upon which we apply different algorithms to generate fractal images. For further more detailed explanation on IFS' and their workings we recommend users to go through these links below:
- [Macintosh IFS manual - Written by Paul Bourke](http://paulbourke.net/fractals/ifs/)
- [Classic Iterated Function Systems - Larry Riddle](https://larryriddle.agnesscott.org/ifs/ifs.htm)
- [Fractals everywhere - MICHAEL F. BARNSLEY](https://www.sciencedirect.com/book/9780120790616/fractals-everywhere)

 Out of many algorithms which generate fractals, our library generates fractals based on Deterministic and Random Iteration algorithms. There are notaions of affine transformations for iterated functions systems (IFS) which are as follows:

<img src="https://github.com/Navaneethnanda/fractal-gen/blob/main/imgs/eqn1.svg" width=250 />
<img src="https://github.com/Navaneethnanda/fractal-gen/blob/main/imgs/eqn4.svg" width=250 />
and

<img src="https://github.com/Navaneethnanda/fractal-gen/blob/main/imgs/eq2.svg" width=250 />
<img src="https://github.com/Navaneethnanda/fractal-gen/blob/main/imgs/eqn3.svg" width=250 />
and

<img src="https://github.com/Navaneethnanda/fractal-gen/blob/main/imgs/CodeCogsEqn.svg" width=350 />

Out of all the most used notation is the third one. Many IFSs are available in similar format to the 3 notation or they can be derived from different forms to the 3rd one some of mostly used notations are below

![Capture](https://user-images.githubusercontent.com/37890718/114451965-84120b80-9bf5-11eb-92a8-e04e05b84c99.PNG)


### Deterministic:
Tabular representation of values `a`, `b`, `c`, `d`, `e`, `f` of 4 Affine transformations.

|       |     a |     b |     c |     d |   e |   f |
|:------|------:|------:|------:|------:|----:|----:|
| set 1 |  0.01 |  0    |  0    |  0.45 |   0 | 0   |
| set 2 | -0.01 |  0    |  0    | -0.45 |   0 | 0.4 |
| set 3 |  0.42 | -0.42 |  0.42 |  0.42 |   0 | 0.4 |
| set 4 |  0.42 |  0.42 | -0.42 |  0.42 |   0 | 0.4 |


### random iteration:
Tabular representation of values `a`, `b`, `c`, `d`, `e`, `f`, `p` of 4 Affine transformations.

|       |     a |     b |     c |    d |   e |    f |   probability |
|:------|------:|------:|------:|-----:|----:|-----:|--------------:|
| set 1 |  0    |  0    |  0    | 0.16 |   0 | 0    |          0.01 |
| set 2 |  0.2  | -0.26 |  0.23 | 0.22 |   0 | 1.6  |          0.07 |
| set 3 | -0.15 |  0.28 |  0.26 | 0.24 |   0 | 0.44 |          0.07 |
| set 4 |  0.85 |  0.04 | -0.04 | 0.85 |   0 | 1.6  |          0.85 |

So all the details we need to generate fractal image are values of `a`, `b`, `c`, `d`, `e`, `f` of an affine traformation in a IFS while using deterministic algorithm and probabilities in addition while using random iteration algorithm. We recommend users to get a good picture on working of IFS' and representations of IFSs before continuing further.

# How to use 

### How to create a `IFS` object and adding eqns.
```py
ifs_obj = Ifs()
lst = [
    [0, 0, 0, 0.16, 0, 0, 0.01], # => [a, b, c, d, e, f, p]
    [0.85, 0.04, -0.04, 0.85, 0, 1.60, 0.85],
    [0.20, -0.26, 0.23, 0.22, 0, 1.60, 0.07],
    [-0.15, 0.28, 0.26, 0.24, 0, 0.44, 0.07],
]

ifs_obj.AddEquations(lst) # Length of all eqns should be equal. Length 7 of random iteration.
                          # length 6 for deterministic.
```

### Printing `IFS` object.
```py
print(ifs_obj)

# equation = 1: [[a = 0.0 b = 0.0]   [[e = 0]  p=0.01
# 	         [c = 0.0 d = 0.16]]  [f = 0]]

# equation = 2: [[a = 0.85 b = 0.04]   [[e = 0.0]  p=0.85
# 	         [c = -0.04 d = 0.85]]  [f = 1.6]]

# equation = 3: [[a = 0.2 b = -0.26]   [[e = 0.0]  p=0.07
# 	         [c = 0.23 d = 0.22]]  [f = 1.6]]

# equation = 4: [[a = -0.15 b = 0.28]   [[e = 0.0]  p=0.07
#  	         [c = 0.26 d = 0.24]]   [f = 0.44]]
```

### Running fractal generating algorithms.

```py
ifs_obj.randomIteration(1_00_000) # Run 1,00,000 iterations.

# For using deterministic algorithm use the below.
ifs_obj.deterministic(Shape.square(), iteration) # deterministic takes Shape and number of iterations as arguments.
                                                 # You can use pre-defined Shape check out Shape class.
                                                 # As of now we have 200-300 points to generate a shape.
```

### Plotting fractal image.
```
ifs_obj.plot()
```

### Output fractal image.

- #### Random iteration output:
<img src="https://github.com/Navaneethnanda/fractal-gen/blob/main/imgs/frac.png" />

- #### Deteministic output:
<img src="https://github.com/Navaneethnanda/fractal-gen/blob/main/imgs/frac1.png" />
