## SSH
# Connecting to an SSH server and remotely executing a command
# In case we want to use public/private keys rather than passwords.
# The following modification is an example of using RSA keys


#!/usr/bin/env python

import paramiko

hostname = '192.168.1.15'
port = 22
username = 'mezbaur'
pkey_file = '/home/mezbaur/.ssh/id_rsa'


if __name__ == '__main__':
  key = paramiko.RSAKey.from_private_key_file(pkey_file)
  s = paramiko.SSHClient()
  s.load_system_hostkeys()
  s.connect(hostname, port, pkey=key)
  stdin, stdout, stderrr = s.exec_command('ifconfig')
  print stdout.read()
  s.close()
