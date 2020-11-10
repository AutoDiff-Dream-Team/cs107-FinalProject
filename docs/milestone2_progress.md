### Milestone 2 Progress Report

#### Assignment

Specifically, for each member of the group, please answer the following questions:

* What tasks has each group member been assigned to for Milestone2.
* What has each group member done since the submission of Milestone1. 

This progress report should be no longer than one page and ideally around 1/2 page. Its main purpose is to help your group
structure project work and delegate tasks. We will be specifically checking to make sure there is equitable distribution of
tasks. All members of the group should contribute code to the core library and all members should contribute to the
documentation.


#### Work to be done for Milestone 2
* Forward mode implementation: 
    * Status: Almost Done, need to check correctness using our test suites
    * Members Contributed: Victor Avram, Diego Zertuche
    * Key components implemented are as follows:
        * AD class defined with the proper constructor (contains the `val` (function value) and `der` (derivative value) attributes)
        * Basic operations along with reverse counterparts (where needed) have been implemented
            * Addition, subtraction, multiplication, division, negation, power, exponential
            * Sine, cosine, tangent
        * The `val` and `der` attributes are updated accordingly
    * Key components to be implemented in next phase:
        * Still developing helper function as Jacobian(), etc. 
            * The user will use the output of this function in a similar fashion to the scalar case (no extra steps needed)
* Test suite:
    * Status: In Progress, close to finish.
    * Members Contributed: Nishu Lahoti, Yuxin Xu
    * Key components implemented are as follows:
        * Unit testing for each overload operator - divided into sections (arithmetic, reverse, and trigonometric)
    * Key components to be implemented in next phase:
        * Tests for multiple input functions
        * Test for jacobian function
* Updated / Extended documentation: 
    * Status: Not started (until Tuesday night)
    * Members Expected to Contribute: Nishu Lahoti
    * Key components to be implemented in next phase:
        * We changed the design of our forward mode implementation, in that we are no longer parsing functions.
        * This change in software design needs to be reflected in our documentation.
* Proposal for additional feature(s)
    * Status: Not started (until Tuesday night)
    * Key components the team is considering implementing:
        * Option 1: Reverse Mode AD
        * Option 2: Computing Hessian Matrix
    * Members Expected to Contribute: Victor Avram, Diego Zertuche, Nishu Lahoti, Yuxin Xu


#### Ways of Working

What are the team's major workstreams? 

* Creating the AutoDiff Class: The forward mode module needs to work as specified by the prompt.
* Testing: Are we properly handling errors? How can we ensure it operates for elementary functions? Can we make the coverage higher?
* Documentation: How can we offer interactive learning for package users?
* Accessibility: How is the code distributed and easily accessed?

How will we work together as a team?

* Collaborating in pairs. We are dividing big categories and assigning two teammates to work together in developing each portion.
* The belief is that working together will lead to better efficiency and higher quality code.