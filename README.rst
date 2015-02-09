#####################
IS 210 Assignment #03
#####################
******************
Synthesizing Tasks
******************

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Lesson: 03
:Points: 
:Due-Date: YYYY-MM-DDT09:00:00

Overview
========

The warm-up tasks this week will focus on general git repository tasks. You'll
be tasked to manipulate files with git's tools prior to submitting the work
through the git pull request workflow.

Instructions
============

The following tasks will either have you interacting with existing files in
the assignment repository or creating new ones on the fly. Don't forget to add
your interpreter directive, utf-8 encoding, and a short docstring with any new
files that you create!

.. important::

    In these exercises, you may, on occasion, come across a task that requres
    you to research or use a function or method not directly covered by the
    course text. Since Python is such a large language it would be impossible
    for the author to have included descriptions of each and every available
    function which would largely duplicate the offical Python documentation.

    A *vital* skill to successful programming is being comfortable searching
    for and using official language documentation sources like the
    `Python String Documentation`_ page. Throughout our coursework we will be
    practicing both the use of the language in practice and the search skills
    necessary to become functional programmers.

Synthesizing Tasks
==================

Task 01
-------

Python's ``.replace()`` string function is a helpful, albeit simple, function
for replacing parts of a string. Complex string replacement is best
accomplished with the ``re`` module, but ``.replace()`` certainly has its place
in the toolbelt as it noticeably outperforms many other string replacement
functions in terms of speed.

Specifications
^^^^^^^^^^^^^^

1.  Open ``task_01.py``

2.  This file **imports** another module whcih makes the attributes of the
    imported module available to the current module. The ``inquisition``
    module imported in ``task_01.py`` provides a constant named ``SPANISH``
    that may be accessed as:

    .. code:: python

        inquisition.SPANISH

3.  Use ``.replace()`` to replace all instances of the word ``surprise`` with
    ``haddock`` and assign the result into a new variable named ``FISHY``

Examples
^^^^^^^^

.. code:: pycon

    >>> print FISHY
    Nobody expects the Spanish Inquisition!
    Our chief weapon is haddock...
    ....

Task 02
-------

Using ``.replace()`` and ``re()`` aren't the only ways to replace values in a
string. This task will challenge you to use a combination of ``.index()``,
slicing, ``len()``, and concatenation, you can achieve the same effect.

Specifications
^^^^^^^^^^^^^^

1.  T11

Examples
^^^^^^^^

.. code:: pycon

    >>> 

Task 03
-------



Specifications
^^^^^^^^^^^^^^

1.  T12

Examples
^^^^^^^^

.. code:: pycon

    >>> 

Task 04
-------



Specifications
^^^^^^^^^^^^^^

1.  T19

Examples
^^^^^^^^

.. code:: pycon

    >>> 

Task 05
-------



Specifications
^^^^^^^^^^^^^^

1.  T20

Examples
^^^^^^^^

.. code:: pycon

    >>> 

Executing Tests
===============

Code must be functional and pass tests before it will be eligible for credit.

Linting
-------

Lint tests check your code for syntactic or stylistic errors To execute lint
tests against a specific file, simply open a terminal in the same directory as
your code repository and type:

.. code:: console

    $ pylint filename.py

Where ``filename.py`` is the name of the file you wish to lint test.

Unit Tests
----------

Unit tests check that your code performs the tested objectives. Unit tests
may be executed individually by opening a terminal in the same directory as
your code repository and typing:

.. code:: console

    $ nosetests tests/name_of_test.py

Where ``name_of_test.py`` is the name of the testfile found in the ``tests``
directory of your source code.

Running All Tests
-----------------

All tests may be run simultaneously by executing the ``runtests.sh`` script
from the root of your assignment repository. To execute all tests, open a
terminal in the same directory as your code repository and type:

.. code:: console

    $ sh runtests.sh

Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Week Two.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01. It is recommended that you run PyLint locally after each file
is edited in order to reduce the number of errors found in testing.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
