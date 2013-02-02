scripts
=======

- Install java, git and maven on the host if they’re not already installed.   
>>> EC2install_script . This script should be part of ec2 userdata input file while creating a file.
Syntax : ec2-run-instances --key K --user-data-file EC2install_script ami-xxxxx

- Build a script that can start / stop / restart the service as a background process on the provided machine.
>>> process_restart.pl

- Capture the sysout & syserr from the process while it’s running, and redirect them to Syslog
>>> syslog_parse.pl 

- Build a tool that periodically checks the service for its health. If a health check fails, the tool should trigger an alert via appropriate channels (e.g. email).  The tool should perform these checks:
>>> process_monitor.pl

I used perl and shell to write the scripts, I was unable to bring the java process on my Ec2 instance due to permission issue being it is in my company AWS account and network hence unable to cover all monitoring requirements.
