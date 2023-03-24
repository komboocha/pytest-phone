# pytest-phone
A school project with pytest framework.

Class Phone models a telephone's behavior. Initializing a new phone reuqires adding a valid phone number -- a 9-digit string beginning with '5' or '6'. 

If an invalid phone number is given at the initialization an exception is raised. 

At the beginning the call_in_progress field is set to False.

There are two methods for phone: start_call() and stop_call() 

Starting a call is successful only if a valid phone number is passed to the start_call() method (it must be a different number than the one already associated with the phone).

As a result the call_in_progress field should change to True. Additionally you can't start a new call while a call is already in progress. Any kind of error raises an exception.

The stop_call() method stops a call (changes call_in_progress to False) if there is a call in progress. If there is no call in progress - an exception is raised.


Exceptions list:
- Invalid phone number: 'Phone number must be a string starting with 5 or 6 consisting of 9 digits'
- Starting a call when another call is already in progress: 'A call is already in progress!'
- Trying to call your own number: 'You cannot call your own number!'
- Trying to stop a call when no call is in progress: 'No call is in progress!'

Test cases have been written for class Phone (test_phone).

