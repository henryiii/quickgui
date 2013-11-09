Introduction
============

Rational
--------
This module was written to be a spiritual successor to the excellent but recently officially abandoned easygui. The purpose of this module, like easygui, is to provide very simple commands that anyone can use to make simple applications and scripts that ask the user a series of questions. Several languages have this functionality built in, like Java and Matlab. This hopefully reduces the learning curve for new programmers needing a simple gui, reduces the difficulty for programmers
not focused on gui design, and is handy for small scripts. Though Python is meant to be object oriented, the basic gui interface should be accessible to programmers coming from other languages, so a primarily function-based approach was used. Many current GUI frameworks are fully object oriented, and this can be daunting for some programmers or overkill for some tasks.

Further, this module attempts to remain independent of both python version (2 or 3) and backend (Qt, Tkinter, Dialog, or plain text). A program using QuickGUI should be able to run all the places python shows up, including terminals, remote systems, or desktops, each time selecting the correct interface.

Finally, this module should follow standard distribution and install procedures, to facilitate it's ease of use.

Design
------
The design chosen was to use several independent implementations in a submodule, and to import those into the main module using a function. This has a low learning curve for new maintainers, avoids a class-based interface, and keeps the code clean. Downsides over using abstract base classes and implementations primarily come from manually making sure each gui function behaves in the same manor. Documentation, defining the basic structure and common arguments to each function, provides the
template on which the four implementations are built. Each function also accepts extra keyword arguments, and any keyword arguments that are not used are ignored. This allows specialization for a backend that does not interfere with another backend.

Alternatives
------------
The Python language includes several simple Tkinter dialogs that cover some of the scope of this project.
