Question - Conduct research to understand how HTTP applications preserve the state
of an application across multiple request-response cycles, especially
concerning user authentication and session management.

Awnser - Each request-response cycle is independant of each other, so some of the ways
to keep consistancy between cycles is with:

-Cookies are a small bit of data stored on the clients browser which are sent with each
request, staying between sessions. Some of the info stored includes authentication tokens
so the user logins automatically. Additionally cookies contain a session id which the
server can map to a users session

-Session IDs, with successful authentication the server makes a session id for the user, 
this info is stored in a cookie or as part of the url. Plus they are long and random to 
prevent guessing and expire after a set time limit or after log out.

-Token-based authentication are signed and encrypted bits of data usually used for API
authentication stored client side.

-Server-side sessions data can be stored server-side in memory, databases or files and 
upon authentication the server creates a session object and assigns a session ID or 
token to the client. Later requests include this retrieve and update session data.

OAuth - Users let third-party applications to see their resources without sharing
credentials. Tokens are used for authentication.

Single Sign On - Allows you to log into multiple websites with just one set of credentials