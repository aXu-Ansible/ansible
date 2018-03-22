#! /usr/bin/python
import csv
with open('./input_new_2.csv') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
           #print (row['Server'])
           print (row['Server'], row['Check-Server'], row['Firewall-Port'])
