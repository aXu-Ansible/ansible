#! /usr/bin/python
import os
import paramiko
import scp
#os.system("/usr/bin/scp"+" xual@10.193.176.6:"+"/etc/hosts "+"/var/tmp/temp1/.")
ssh1=paramiko.SSHClient()
ssh1.load_system_host_keys()
ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh1.connect('sdcgigdcapmdw02',username='xual')
with scp.SCPClient(ssh1.get_transport()) as scp1:
   #scp.put('test.txt', 'test2.txt')
   scp1.get('/etc/ansible/hosts','/var/tmp/temp2/.')
scp1.close()
print ("testing")
      
