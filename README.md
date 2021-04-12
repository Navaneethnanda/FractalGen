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


Out of all the most used notation is the third one. Many IFSs are available in similar format to the 3 notation or they can be derived from different forms as below

![Capture](https://user-images.githubusercontent.com/37890718/114451965-84120b80-9bf5-11eb-92a8-e04e05b84c99.PNG)


Deterministic:
![Capture1](https://user-images.githubusercontent.com/37890718/114452267-e2d78500-9bf5-11eb-85c0-24fd4b97fbd1.PNG)

random iteration:
![Capture2](https://user-images.githubusercontent.com/37890718/114452284-e834cf80-9bf5-11eb-90db-368157db850d.PNG)

So all the details we need to generate afrctal image are values of a,b,c,d,e,f while using determininstic algorithm and probabilities in addition while using random iteration algorithm. We recommend users to get a good picture working of ifs or format of ifs before continuing further.

#How to use 
First initialize IFS object and pass IFSs method AddEquations in the below format:
object = IFS()
eqns=[[a1,b1,c1,d1,e1,f1],#probabilities should be added f u intent to use random iteration algorithm [[a1,b1,c1,d1,e1,f1,p1],[a2,b2,c2,d2,e2,f2,p2],...[an,bn,cn,dn,en,fn,pn]]
[a2,b2,c2,d2,e2,f2],
.
.
.
[an,bn,cn,dn,en,fn]]
object.AddEquations(eqns)
beta kkada nunchi esei

