# Learning Objectives
What is a server
Where servers usually live
What is SSH
How to create an SSH RSA key pair
How to connect to a remote host using an SSH RSA key pair
The advantage of using #!/usr/bin/env bash instead of /bin/bash

# Tasks
Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

Requirements:

Only use ssh single-character flags
You cannot use -l
You do not need to handle the case of a private key protected by a passphrase

1. Create an SSH key pair
Write a Bash script that creates an RSA key pair.

Requirements:

Name of the created private key must be school.
The number of bits in the created key should be 4096.
The created key must be protected by the passphrase betty.
2. Client configuration file
Your machine has an SSH configuration file for the local SSH client. Configure it to use the private key ~/.ssh/school and refuse to authenticate using a password.

3. Let me in!
Add the provided SSH public key to your server so that others can connect using the ubuntu user.

Copyright and License
© 2023 ALX, All rights reserved.
