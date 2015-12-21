#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Student Data"""

import json
import pprint


#Reads and assigns the schools json file
print 'Loading school file...'
fhandler = open('schools1.json')
schools_data = json.load(fhandler)
fhandler.close()
#pprint.pprint(schools_data['data'])



#Reads and assigns the students json file
print 'Loading student file...'
fhandler = open('students1.json')
student_data = json.load(fhandler)
fhandler.close()
#pprint.pprint(student_data)

print 'Done.'


#Creates dict with the average scores by school
stu_result_list = []
dict1 = {k: d.values() for k,d in student_data['data'].items()}
for datalist in dict1.itervalues():
    p = datalist[2], datalist[1]
    stu_result_list.append(p)

stu_avg = {}
for k, v in stu_result_list:
    stu_avg.setdefault(k,[]).append(v)

for key in stu_avg:
    stu_avg[key] = [float((sum(stu_avg[key]))) / (len(stu_avg[key]))]

#pprint.pprint(stu_avg)

#Creates dict with schools and their average spend per student
school_list = []
for item in schools_data['data']:
    y = item['school_id'], item['per_student_spending']
    school_list.append(y)

school_avg = {}
for k, v in school_list:
    school_avg.setdefault(k,[]).append(v)

#pprint.pprint(school_avg)

#Merges the dicts and calculates the school with best ratio by creating rank value
DICTS = [stu_avg, school_avg]
MASTERDICT = {}
for k in stu_avg.iterkeys():
    MASTERDICT[k] = list((MASTERDICT[k]) for MASTERDICT in DICTS)
    MASTERDICT[k] = (float(MASTERDICT[k][0][0]) / MASTERDICT[k][1][0])*10000
    
schoolrank = {v:k for k,v in MASTERDICT.items()}
bestschoolratio = schoolrank[max(schoolrank)]


#Creates dict with schools and districts
district_list = []
for item in schools_data['data']:
    y = item['school_id'], item['district_code']
    district_list.append(y)

districtsdict = {}
for k, v in district_list:
    districtsdict.setdefault(k,[]).append(v)


#Merges dicts and calculates district rank 
DICTS1 = [MASTERDICT, districtsdict]
COMBODICT = {}
for k in MASTERDICT.iterkeys():
    COMBODICT[k] = list((COMBODICT[k]) for COMBODICT in DICTS1)

rest = {}
for k, v in COMBODICT.iteritems():
    rest[k] = [rest[v][1][0]]
    

#pprint.pprint(COMBODICT)

#inv = {}
#for k, v in COMBODICT.iteritems():
   # print  v
    #for i in COMBODICT[k]:
       #newdict = sum(v)
    #inv[v] = [inv[k]]
    #   k = inv.setdefault((v[1][0]), ([v[0]]))
   #keys.append((v[0]))

#for key in inv:
   #inv[k] = [inv[v[0]]]
   #inv.setdefault(k,[]).append(v)
#for i in inv:
    





#pprint.pprint(inv)

    

