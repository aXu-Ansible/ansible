#!/usr/bin/python
import csv
import yaml
in_file  = open('./input_new_5.csv', "r")
out_file = open('./yaml_file.yaml', "w")
items = []

def convert_to_yaml(line, counter):
    item = {
        'id': counter,
        'title_english': line[0],
        'title_russian': line[1]
    }
    items.append(item)

try:
    reader = csv.reader(in_file)
    next(reader) # skip headers
    for counter, line in enumerate(reader):
        convert_to_yaml(line, counter)
    out_file.write( yaml.dump(items, default_flow_style=False) )

finally:
    in_file.close()
    out_file.close()
