## SSH
# Connecting to an SSH server and remotely executing a command
# password to be assigned later


#!/usr/bin/env python

import paramiko

hostname = '192.168.1.15'
port = 22
username = 'mezbaur'
password = ''

if __name__ == '__main__':
  paramiko.util.log_to_file('paramiko.log')
  s = paramiko.SSHClient()
  s.load_system_hostkeys()
  s.connect(hostname,port,username,password)
  stdin, stdout, stderrr = s.exec_command('ifconfig')
  print stdout.read()
  s.close()


