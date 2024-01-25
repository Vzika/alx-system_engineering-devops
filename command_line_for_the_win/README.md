 Command Line for the Win (CLFTW)

  2 Welcome to the Command Line for the Win repository! This repository contains a collection of exercises aimed at enhancing command-line skills and proficiency.
  3  It's designed to help users become more comfortable and proficient in using the command line for various tasks.
  4
  5 Description
  6 CMD CHALLENGE a pretty cool game challenging you on Bash skills. Everything is done via the command line and the
  7 questions are becoming increasingly complicated. It’s a good training to improve your command line skills!
  8
  9 Using sftp command line to tranfer files (screenshots) from the local machine to a remote srver. Once the screenshots are transferred,
 10 you can proceed to push the screenshots to GitHub.
 11
 12 Usage:
 13 1) Ready your files that are to be transferred, in this case we transferred screenshots. Files can be anywhere in your local machine.
 14
 15 2) Get your client remote server username, hostname and password ready for SFTP via ssh connection user@host.
 16
 17 3) Open your local machine terminal and enter your remote server sftp command (sftp username@hostname), It will ask for an option,
 18 enter yes and input your server password to connect, then you will begin with a sftp prompt.
 19
 20 4) Use the "put" command to uppload your file to the server, e.g put <file pathname> <srver destination pathname>. server dest
 21 pathname can be nothing if you are on the current working directory.
 22
 23 5) You can use the "get" command to download files from the server
 24
 25 6) Use the "exit" command to end the process.
 26
 27 Author:
 28 Ndukauba(Obasi) Ngozi
