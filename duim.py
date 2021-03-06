#!/usr/bin/env python3

import subprocess, sys
import os
import argparse



'''
OPS435 Assignment 2 - Summer 2021
Program: duim.py 
Author: Manveer Dhami
The python code in this file (duim.py) is original work written by
Manveer Dhami. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: Returns all directory along with the size in a bar graph.

Date: July 26th 2021
'''

def parse_command_args():
    #"Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="DU Improved -- See Disk Usage Report with bar charts",epilog="Copyright 2021")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    args = parser.parse_args()


def percent_to_graph(percent, total_chars):
   # "returns a string: eg. '##  ' for 50 if total_chars == 4"
    graph = percent/100
    graph = graph * total_chars
    graph = round(graph)
    bar=""
    space=""
    p = 0
    i = 0
    end = total_chars - graph
    
    while p != graph:
        bar = bar + "#"
        p = p + 1
    finish = "["+ bar
    
    while i != end:
        space = space + " "
        i = i + 1
    finish = finish + space + "]"    
    
    return finish

def call_du_sub(location):
    #"use subprocess to call `du -d 1 + location`, rtrn raw list"
    cmd = subprocess.Popen('du -d 1 ' + location, shell=True, stdout=subprocess.PIPE)
    take1 = []
    take1 = cmd.stdout.readlines()
    take2 = []
    for i in take1:
        take2.append(i.decode('utf8', errors='strict').strip())
    return take2

def create_dir_dict(raw_dat):
   # "get list from du_sub, return dict {'directory': 0} where 0 is size"
    fol = {}
    for x in raw_dat:
        d = x.split("\t")
        k = d[1]
        v = int(d[0])
        fol.update({k:v})
    return fol


if __name__ == "__main__":
    #take input from user and get directory size
    sub = call_du_sub(sys.argv[1])
    dit = create_dir_dict(sub)
    total_size = dit[sys.argv[1]]
    total_size = total_size / 1000
    #print(dit)
    holder = []
    val = []
    p=0
    for value in dit:
        holder.append(dit[value])
        val.append(value)
    for i in holder:
        percent = ((int(i) / 1000) / int(total_size)) * 100
        print(val[p] + " " + percent_to_graph(percent ,int(total_size)))
        p = p + 1

