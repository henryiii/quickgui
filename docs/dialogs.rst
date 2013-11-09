Dialogs
=======

Questions
---------

The following dialogs ask the user a question. All dialogs have an optional title parameter.

.. function:: ask_yn(msg='Answer yes or no',title)
              ask_ok(msg='Continue?')
   
   This will ask the user a yes/no question, and will return True or False.
   Canceling returns False, and defaults to True.

.. function:: ask_opts(msg='Choose an option',opts=['one','two'])
              ask_opts_multi(msg='Choose options',opts=['one','two'])

   This will present a list of options to the user, allowing them to choose one. The one chosen will be returned. If an (ordered) dict is passed as options, the value will be displayed, and the key returned.
   The options may be displayed as a list or as buttons, depending on the number of options and the length to display.
   The multi version allows selection of several options.

.. function:: ask_pass(msg='Enter a password:')
              ask_user(msg='Enter a username and password:',user='User',password='Password')

   Asks the user for a password, or username and password. Returns the password, or a tuple username,password.

.. function:: ask(msg='Enter something',valitator=str)

   Asks the user for a value. Specializes for different validations. The dialog will return validation(input).

Information
-----------

.. function:: tell(msg='This is a dialog',type='ok')

   Tells the user something. Type allows you to make it a warning, etc. Changes to adapt to any amount of information.

.. function:: wait(item, number=0, msg='Processing...')
              wait_show(item, number=0, msg='Processing...')
   
   If an iterator is passed, will iterate, updating the show dialog with the result of the iterator, or the first part of the result of the iterator for iteerators that produce tuples, if the show version is used. If the number argument is non-zero, will show percent left. 
   If a function is passed, calls the function and waits for a result.
   The msg can contain `{num}`, `{tot}`, `{timeleft}`, `{timepassed}`, and `{totaltime}`. Num will be updated regardless of the total.

Files
-----

.. function:: file_get(msg='Get a file', multi=False, types=('All','*'))
   
   Get a file to open. Only returns a list if multi is True. 

.. function:: file_save(msg='Save a file', types=('All','*'), ext='')

   Get a name to save to. Propts for ooverwrite. Forces ext.

.. function:: file_dir(msg='Save a file')

   Get a directory name.

Multipurpose
------------

.. function:: multi_question(items)

   Takes a list of tuples, with (msg,key,validator).


Validators
----------

Valid validators are:

:str: A normal string.
:int: An integer
:float: A number
:'pass': A password


