# LYZA

![Python package](https://github.com/osolmaz/lyza/workflows/Python%20package/badge.svg)

This project grew out of dissatisfaction with not being able to control what is
going on under the hood with most finite elements packages. It was inspired by
[FEniCS](https://fenicsproject.org/).

## Installation

For basic usage:

    cd lyza
    sudo python setup.py install


For development:

    cd lyza/
    sudo pip install --editable .

## Examples

To run an example, simply go into the corresponding directory and execute the
Python file inside:

```
cd examples/hyperelasticity
python hyperelasticity.py
```

The blog posts given below contain the formulations for some of the examples.

| Example | Blog post |
|-|-|
|[Poisson](/examples/poisson)| [Linear Finite Elements](https://solmaz.io/notes/linear-finite-elements/)|
|[Linear Elasticity](/examples/linear_elasticity)| [Vectorial Finite Elements](https://solmaz.io/notes/vectorial-finite-elements/)|
|[Cahn Hilliard](/examples/cahn-hilliard)| [Nonlinear Finite Elements](https://solmaz.io/notes/nonlinear-finite-elements/)|
|[Hyperelasticity](/examples/hyperelasticity)| [Variational Formulation of Elasticity](https://solmaz.io/notes/variational-formulation-elasticity/)|
|[Nonlinear Poisson](/examples/nonlinear_poisson)| [Nonlinear Finite Elements](https://solmaz.io/notes/nonlinear-finite-elements/)|
|[Reaction-advection-diffusion](/examples/reaction_advection_diffusion)| [Time-Dependent Finite Elements](https://solmaz.io/notes/time-dependent-finite-elements/)|

The examples are specified and solved in very simple domains, but it is possible
to read in or generate arbitrary meshes.
