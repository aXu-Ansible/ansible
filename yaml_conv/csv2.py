#! /usr/bin/python
import csv
with open('./data1.csv') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
           #print (row)
           print (row['Server'])
           #print (row['Server'], row['Check_Server'], row['Firewall_Port'])
