Command Line for the Win (CLFTW)
Welcome to the Command Line for the Win repository! This repository contains a collection of exercises aimed at enhancing command-line skills and proficiency.
 It's designed to help users become more comfortable and proficient in using the command line for various tasks.

Description
CMD CHALLENGE a pretty cool game challenging you on Bash skills. Everything is done via the command line and the 
questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

Using sftp command line to tranfer files (screenshots) from the local machine to a remote srver. Once the screenshots are transferred, 
you can proceed to push the screenshots to GitHub.

Usage:
1) Ready your files that are to be transferred, in this case we transferred screenshots. Files can be anywhere in your local machine.

2) Get your client remote server username, hostname and password ready for SFTP via ssh connection user@host.

3) Open your local machine terminal and enter your remote server sftp command (sftp username@hostname), It will ask for an option, 
enter yes and input your server password to connect, then you will begin with a sftp prompt.

4) Use the "put" command to uppload your file to the server, e.g put <file pathname> <srver destination pathname>. server dest 
pathname can be nothing if you are on the current working directory.

5) You can use the "get" command to download files from the server

6) Use the "exit" command to end the process.

Author:
Ndukauba(Obasi) Ngozi
