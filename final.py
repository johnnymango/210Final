#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Student Data"""

import json
import pprint


#Reads and assigns the schools json file
fhandler = open('schools1.json')
schools_data = json.load(fhandler)
fhandler.close()
pprint.pprint(schools_data)

print '-'*25

#Reads and assigns the students json file

fhandler = open('students1.json')
student_data = json.load(fhandler)
fhandler.close()
pprint.pprint(student_data)

print '-'*25





