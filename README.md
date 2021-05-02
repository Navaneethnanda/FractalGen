# Fractal-gen
Fractal-gen is a open library which can be used to generate, experiment and create fractal images using IFSs. IFSs are Iterated Function Systems which are used in one of the methods in constructing fractals. IFSs are simply set of Affine equations upon which we apply different algorithms to generate fractal images. For further more detailed explanation on IFSs and their workings we recommend users to go through these links below:
1. http://paulbourke.net/fractals/ifs/
2. https://larryriddle.agnesscott.org/ifs/ifs.htm
3. https://www.sciencedirect.com/book/9780120790616/fractals-everywhere

 Out of many algorithms which generate fractals, our library generates fractals based on Deterministic and Random Iteration algorithms. 
 
 There are many ways of describing the affine transformations for iterated functions systems (IFS) which are as follows:

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

|       |     a |     b |     c |     d |   e |   f |
|:------|------:|------:|------:|------:|----:|----:|
| set 1 |  0.01 |  0    |  0    |  0.45 |   0 | 0   |
| set 2 | -0.01 |  0    |  0    | -0.45 |   0 | 0.4 |
| set 3 |  0.42 | -0.42 |  0.42 |  0.42 |   0 | 0.4 |
| set 4 |  0.42 |  0.42 | -0.42 |  0.42 |   0 | 0.4 |


### random iteration:

|       |     a |     b |     c |    d |   e |    f |   probability |
|:------|------:|------:|------:|-----:|----:|-----:|--------------:|
| set 1 |  0    |  0    |  0    | 0.16 |   0 | 0    |          0.01 |
| set 2 |  0.2  | -0.26 |  0.23 | 0.22 |   0 | 1.6  |          0.07 |
| set 3 | -0.15 |  0.28 |  0.26 | 0.24 |   0 | 0.44 |          0.07 |
| set 4 |  0.85 |  0.04 | -0.04 | 0.85 |   0 | 1.6  |          0.85 |

So all the details we need to generate fractal image are values of a,b,c,d,e,f of an affine traformation in a IFS while using deterministic algorithm and probabilities in addition while using random iteration algorithm. We recommend users to get a good picture on working of IFSs and representations of IFSs before continuing further.

# How to use 
First initialize IFS object and pass IFSs Through AddEquations method like shown below:

    object = IFS()
    eqns=[[a1,b1,c1,d1,e1,f1],
    [a2,b2,c2,d2,e2,f2],
    .
    .
    [an,bn,cn,dn,en,fn]]
    #probabilities should be added if your intent is to use random iteration algorithm [[a1,b1,c1,d1,e1,f1,p1],[a2,b2,c2,d2,e2,f2,p2],...     [an,bn,cn,dn,en,fn,pn]].
    object.AddEquations(eqns)
    
