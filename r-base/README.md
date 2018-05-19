##Files
r-base-dep - Dependencies for R compilation (Ubuntu 18.04)
r-x.x.x - Compiled R runtime files

sample.r - Sample R script that takes a path to CSV File as an argument
run.sh - Command to Invoke sample.r passing a Dataset

Dockerfile - testing packaging R within a redistributable Container image,
	for environments without accessible Package manager (apt / yum)

##Complilation
Build 2018-05-19
R-3.5.0
Ubuntu 18.04 LTS (Bionic Beaver)
gcc version 7.3.0 (Ubuntu 7.3.0-16ubuntu3)

###x86_64 GNU/Linux indicates that you've a 64bit Linux kernel running.
### If you use see i386/i486/i586/i686 it is a 32 bit kernel
$ uname -a
x86_64 GNU/Linux
