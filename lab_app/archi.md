The archi will be as follow :

There is a builtin User class

There is a Machine class that has an id, a type, a password and a name

There is a Results class that will manage the results, for the moment just a textfield

There is a Session class that will have a docker, a token, a user foreign key, a machine type a flag and a Result (null on the creation)

User will login with email/username and password

Machine will login with id and password

User can create session, and manage the session he already created.

for the manage session part the user can :
- cancel a session if it hasen't been run
- stop a session and get results (if handled by the docker)

Machine can get session info and run it (when it run a session, it will put a flag on the session so that it will not be taken by another machine).

If a session can't be run (or get errors) the machine put an error flag a and send back results with the errors logs.

When a machine finish the session, it will create a Results accessible to the user and put a finish flag on the session

The session flags are :
- Waiting for machine
- Running
- Finished
- Pending Stop
- Stoped
- Error

To stop or finish a session, a machine must create a Result and attached it to the session

Ideas :
- the file that will be send back to the results will be register on a specific folder so that it will be easier for the machine to choose what to send.
- all the log will be saved on a file and sent back with the results

