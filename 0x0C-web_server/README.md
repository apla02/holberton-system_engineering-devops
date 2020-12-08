# 0x0C-web_server

## General

> - What is the main role of a web server : serve static content
> - What is a child process: a process create from other process
> - Why web servers usually have a parent process and child processes
    So that the web server can dynamically change the number of child process
    to accommodate the volume of requests to be processed
> - What are the main HTTP requests: GET, POST, HEAD


## DNS

> - What DNS stands for
    Stands for "Domain Name System.". DNS translates domain names into IP addresses,
    allowing you to access an Internet location by its domain name.

> - What is DNS main role
    because humans are not good at remembering long sequences of numbers (IP address)

## DNS Record Types

> - A : adress IP record
> - CNAME : canonical name (domain) record
> - TXT: text record
> - MX : mail exchanger record 

# Tasks

##  0. Transfer a file to your server mandatory

> Write a Bash script that transfers a file from our client to a server:

> - Requirements:

> - Accepts 4 parameters
>> - The path to the file to be transferred
>> - The IP of the server we want to transfer the file to
>> - The username scp connects with
>> - The path to the SSH private key that scp uses
>> - Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
>> - scp must transfer the file to the user home directory ~/
>> - Strict host key checking must be disabled when using scp




