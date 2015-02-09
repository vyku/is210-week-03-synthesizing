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
:Points: 15
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

1.  Open ``task_02.py``

2.  Use a combination of ``.index()``, slicing, ``len()``, simple addition,
    and string concatenation to programmatically replace the first instance of
    the word ``Spanish`` with ``Flemish`` in ``inquisition.SPANISH``

3.  Save the result to a new variable named ``FLEMISH``

.. hint::

    Start by creating a variable for the string you want to replace
    (``'Spanish'``) and then calculating its length

.. hint::

    You can use variables containing integers as positions in a slice
    operation.

.. Note::

    While this method may, at first, seem very convoluted, there are some
    common use-cases for it in functions and loops.

Examples
^^^^^^^^

.. code:: pycon

    >>> print FISHY
    Nobody expects the Flemish Inquisition!
    Our chief weapon is surprise...
    ....

Task 03
-------

The slice operation's *step* or *stride* parameter may be used to reverse a
string.

Specifications
^^^^^^^^^^^^^^

1.  Open ``task_03.py``

2.  Use the third parameter of the slice syntax to reverse the order of the
    characters in the ``NAPOLEON`` variable and save the result into a new
    variable named ``REVERSED``

3.  Use the ``.lower()`` method to set ``REVERSED`` to lowercase and save
    the result back onto itself.

Examples
^^^^^^^^

.. code:: pycon

    >>> print REVERSED
    .able was i ere ,i saw elba

Task 04
-------

While concatenation and slicing are certainly acceptable ways to manipulate
strings, the preferred means of injecting data into strings is via the
``.format()`` method.

Specifications
^^^^^^^^^^^^^^

1.  Open ``task_04.py``

2.  Modify the ``NEWS`` variable so that the last formatting string (``{1}``)
    will display its value as a 6-digit number padded with zeros.

3.  Use the ``.format()`` method to format the ``NEWS`` string variable and
    assign the following values:

    -   ``{friend}`` => ``FNAME``
    -   ``{0}`` => ``NTYPE``
    -   ``{1}`` => ``RNUM``

    Save the result into a new variable named ``EMAIL``

Examples
^^^^^^^^

.. code:: pycon

    >>> print EMAIL
    Hi Pat! I have *amazing* news! I won the raffle with number 000042!

Task 05
-------

Object identity using ``is`` is another form of comparison operation. Unlike
its cousin the equality operator (``==``), ``is`` tests if the two things being
compared are the exact same object. In many languages this can be thought of as
the strict comparison operator (``===``). This operator can also be modified by
the ``not`` logical operator to invert the response (eg, ``is not``). This is
sometimes a very important distinction as you'll see below.

Specifications
^^^^^^^^^^^^^^

1.  Open ``task_05.py``

2.  Currently, this code is broken. when ``is_empty()`` is passed an empty
    string it throws an error. Because an empty string still has a length (0),
    it should instead report ``True``

3.  fix the ``is_empty()`` function by changing one operator on one line of
    code so that it only raises an exception when it's passed a non-sequence
    data type, like an integer. Otherwise, it should correctly report whether
    or not the passed argument has no length.

.. hint::

    Review the alternative values of booleans.

.. hint::

    If you use ``python -i`` to run this code you can use the interactive
    command line to call ``is_empty()`` and pass it any type of data you want
    including empty string (``is_empty('')``), non-empty strings
    (``is_empty('apple')``), and integers (``is_empty(2)``).

.. hint::

    Read the docstrings for both functions to get a sense of what they do.

.. important::

    Much of what you see in this file may be new and that's intended. A
    critical skill for programmers of all aptitudes is the ability to
    investigate complex codebases and identify a particular feature or fix that
    is already within the scope of your current skillset. Many codebases are so
    large it is literally impossible for any one person to have a complete
    understanding of the system and in such situations, it is important to have
    the confidence and experience necessary to successfully skim through the
    unnecessary components.

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
