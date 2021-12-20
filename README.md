# iamautodiff - A Package for Automatic Differentiation

### Members: Diego Zertuche, Nishu Lahoti, Victor Avram, Yuxin Xu


[![Build Status](https://travis-ci.com/AutoDiff-Dream-Team/cs107-FinalProject.svg?token=nyPv3TajU2phyRWmUVDr&branch=master)](https://travis-ci.com/AutoDiff-Dream-Team/cs107-FinalProject)
[![codecov](https://codecov.io/gh/AutoDiff-Dream-Team/cs107-FinalProject/branch/master/graph/badge.svg?token=ZPE1U9QCPV)](https://codecov.io/gh/AutoDiff-Dream-Team/cs107-FinalProject)


### Introduction
---

Automatic differentiation (AD) encompasses a suite of tools used to compute the derivatives of functions, evaluate the functions at specified values, and evaluate the functions' derivates at specified values. In a situation where analytically deriving the derivative of compicated functions is not feasible (within the user's limitations), AD guarantees to return the exact solution in theory. In practice, rounding errors may compound given that AD performs a series of elementary operations.  

### Documentation
---

For documentation and how-to-use, please reiew our [documentation notebook](https://github.com/AutoDiff-Dream-Team/cs107-FinalProject/blob/master/docs/documentation.ipynb).

### Modules
---

We have three modules within our package `Auto_diff`.
*  `FD`: a module that contains the following class:
    * The `FD` class used for instatiating an `FD` object, which is used to perform the forward mode of automatic differentiation and produces the numerical output.
*  `RD`: a module that contains the following class:
    * The `RD` class used for instatiating an `RD` object, which is used to perform the reverse mode of automatic differentiation and produces the numerical output.
*   `jacobian`: a module that contains the following function:
    * The function`Jacobian` used for handling functions of multiple inputs. This function takes as an argument a list defining the values for each input for the given function and returns a list of `FD` objects.
*  `test_basic_v2`: a module that tests all the elementary functions (addition, multiplication, power, etc) and functions like `get_value` and `get_derivative` for the forward mode. 
*  `test_rd`: a module that tests all the elementary functions (addition, multiplication, power, etc) and functions like `get_value` and `get_gradient` for the reverse mode. 
*  `test_jacobian`: a module that tests function `Jacobian` on a single function and multiple functions.

### Broader Impact and Inclusivity Statement
---

In the closing years of the 2010s, the technology industry came under fire for turning a blind eye to the unintended consequences created from new-age technology. The classic example is that of Facebook and the divisiveness the United States experienced in the 2016 and 2020 elections. This statement aims to reflect upon the issue how our automatic differentiation package could have unintended, exclusionary consequences.

Our development team operated under the assumption that users of our package have a basic familiarity with object oriented programming, calculus and mathematical terminologies in English. While we built the package to have a smooth user experience, the software functions inside of a python environment, and rides upon the basic assumption that users have fundamental programming, mathematical capabilities and some basic english. While this was by design, the package does, as a result, exclude anyone without these fundamental abilities, of which there is a large portion of the United States / Cambridge / Harvard community. In the case that a student or professional aimed to solve a complex automatic differentiation problem, and did not have basic capabilities in python, they would be excluded from our package.

A potential solution that would make our package more inclusive is the development of a web interface , similar to the one demo'd in class, through which any user hoping to compute a complex derivative to machine precision could simply enter their input functions and values and get a quick and easy result. This could be an extension for the future of our package.

We had some additional considerations on how this package could be more inclusive. To start, we could expand it beyond python and make it accessible in different languages. This package is meant for python developers, a subset of the coding population which may be relatively young and early-career. For developers later in their career that have not necessarily learned python (or earlier, for that matter) we would need a package that speaks their native coding language. In this way, we could expand our software. 
