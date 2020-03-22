## Telegraphy
**Summary**
A simple client/server chat made using Python - (Version 3.7.4)

**Details**
A "chatroom" like application created in Python with the help of the socket library. Unlike traditional chatrooms, users can only send one message at a time, and then they must wait for a response from the other user. In order for this program to work, you must launch the "Server" before the client. Furthermore, you may need to make an exception in both your devices firewalls.

**Extras**
An issue occured when resolving the IP using the socket library which would result in the IP (127.0.0.1) being returned. In order to fix this I needed to use a work around, which can be found in the resolve.py file.
