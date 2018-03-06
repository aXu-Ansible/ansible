#! /usr/bin/python
import os
import paramiko
import scp
import sys
#os.system("/usr/bin/scp"+" xual@10.193.176.6:"+"/etc/hosts "+"/var/tmp/temp1/.")
server_name="server1"
def get_file_from_server(host_ip1,server_name_1):
#global server_name
  ssh1=paramiko.SSHClient()
  ssh1.load_system_host_keys()
  ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh1.connect(host_ip1,username='sftp_user')
  print ("test")
  sys.exit(0)
  with scp.SCPClient(ssh1.get_transport()) as scp1:
   #scp.put('test.txt', 'test2.txt')
   scp1.get('/tmp/info.csv','/tmp/'+server_name_1+'-info.csv')
  scp1.close()
def get_servername():
  global server_name
  with open('./hosts.list') as f:
    for line in f:
       print line 
       host_ip=line.split(" ")[0]
       server_name1=line.split(" ")[1]
       print host_ip
       print server_name1
       #sys.exit(0)
       get_file_from_server(host_ip,server_name1)
  f.close()
  #return host_ip
#####################################################

get_servername()
sys.exit(0)
#ssh1=paramiko.SSHClient()
#ssh1.load_system_host_keys()
#ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print ("testing")
      
