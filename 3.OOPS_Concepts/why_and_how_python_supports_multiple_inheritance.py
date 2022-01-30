"""Case study on multiple inheritance in python

As we all know that most of the prgramming languages does not support multiple inheritance becasue of 
the daimond problem.

What is the daimond problem?

The diamond problem occurs when two classes have a common ancestor, and 
another class has both those classes as base classes, for example:

"""


class A:
    def do_thing(self):
        print('From A')


class B(A):
    def do_thing(self):
        print('From B')


class C(A):
    def do_thing(self):
        print('From C')


class D(B, C):
    pass


d = D()
d.do_thing()

"""
In some languages, because of how inheritance is implemented, when you call d.do_thing(), 
it is ambiguous whether you actually want the overridden do_thing from B, or the one from C.

"""

"""
Python doesn't have this problem because of the method resolution order. Briefly, when you inherit from multiple classes, if their method names conflict, 
the first one named takes precedence. Since we have specified D(B, C), B.do_thing is called before C.do_thing.
"""
# https://stackoverflow.com/questions/56217501/question-related-to-super-with-init/56217632#56217632
# https://stackoverflow.com/questions/56361048/what-is-the-diamond-problem-in-python-and-why-its-not-appear-in-python2

