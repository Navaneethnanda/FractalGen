# fractal-gen
Fractal gen is a open library which can be used to generate, experiment and produce fractal images using IFS. IFSs are Iterated Function Systems which is a method in construting fractals. IFSs are simply set of equations upon which we apply algorithms to generate fractal images. For further more detailed explanation we reccommend users to go through these links below:
1. http://paulbourke.net/fractals/ifs/
2. https://larryriddle.agnesscott.org/ifs/ifs.htm

 There are many algorithms to generate fractals our library generates fractals based on Deterministic and random iteration algorithms. 
 
 There are many ways of describing the affine transformations for iterated functions systems (IFS) as follows:

1. x = r cos(θ) x + s sin(θ) y + h 
2. y = -r sin(θ) x + s cos(θ) y + k

and 

1. xn+1 = a xn + b yn + c
2. yn+1 = d xn + e yn + f

and 

1. | xn+1 |      | a   b |   | xn |     | e |
2. |      |   =  |       | * |   |  +   |   |
4. | yn+1 |      | c   d |   | yn |     | f |


Out of all the most used notation is the third one. We  can get IFSs similar to 3 notation or they can be derived from different forms as below

