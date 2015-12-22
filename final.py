#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Student & School Data"""

import json


# Reads and assigns the schools json file.
print 'Loading schools file...'
FHANDLER = open('schools.json')
SCHOOLS_DATA = json.load(FHANDLER)
FHANDLER.close()
print 'Done.'


# Reads and assigns the students json file.
print 'Loading student file...'
FHANDLER = open('students.json')
STUDENT_DATA = json.load(FHANDLER)
FHANDLER.close()
print 'Done.'


# Creates dict with the average student scores by school.
STU_RESULT_LIST = []
DICT1 = {k: d.values() for k, d in STUDENT_DATA['data'].items()}
for datalist in DICT1.itervalues():
    p = datalist[2], datalist[1]
    STU_RESULT_LIST.append(p)

STU_AVG = {}
for k, v in STU_RESULT_LIST:
    STU_AVG.setdefault(k, []).append(v)

for key in STU_AVG:
    STU_AVG[key] = [float((sum(STU_AVG[key]))) / (len(STU_AVG[key]))]


# Creates dict with schools and their average spend per student.
SCHOOL_LIST = []
for item in SCHOOLS_DATA['data']:
    y = item['school_id'], item['per_student_spending']
    SCHOOL_LIST.append(y)

SCHOOL_AVG = {}
for k, v in SCHOOL_LIST:
    SCHOOL_AVG.setdefault(k, []).append(v)


# Merges the student and schooled avg dicts and calculates best school ratio.
DICTS = [STU_AVG, SCHOOL_AVG]
MASTERDICT = {}
for k in STU_AVG.iterkeys():
    MASTERDICT[k] = list((MASTERDICT[k]) for MASTERDICT in DICTS)
    MASTERDICT[k] = (float(MASTERDICT[k][0][0]) / MASTERDICT[k][1][0])*10000

SCHOOLRANK = {v: k for k, v in MASTERDICT.items()}
BESTSCHOOLRATIO = SCHOOLRANK[max(SCHOOLRANK)]


# Creates dict with schools and districts.
DISTRICT_LIST = []
for item in SCHOOLS_DATA['data']:
    y = item['school_id'], item['district_code']
    DISTRICT_LIST.append(y)

DISTRICTSDICT = {}
for k, v in DISTRICT_LIST:
    DISTRICTSDICT.setdefault(k, []).append(v)


# Merges dicts and calculates the best distict ratio.
DICTS1 = [MASTERDICT, DISTRICTSDICT]
COMBODICT = {}
for k in MASTERDICT.iterkeys():
    COMBODICT[k] = list((COMBODICT[k]) for COMBODICT in DICTS1)

DISTRICTRANK = {}
for k, v in COMBODICT.iteritems():
    k = DISTRICTRANK.setdefault(v[1][0], ([]))
    k.append((v[0]))

for k, v in DISTRICTRANK.iteritems():
    DISTRICTRANK[k] = [((sum(DISTRICTRANK[k])) / len(DISTRICTRANK[k]))]

RANK = {v[0]: k for k, v in DISTRICTRANK.items()}
BESTDISTRICTRATIO = RANK[max(RANK)]


def get_result(data):
    """This function returns the results of the data files.

    Args:
        data(str): 'school' or 'district'

    Returns:
        String: A formatted string.

    Examples:
        >>> get_result('school')
        The school with the best ratio is PS0664.
    """
    if data == 'school':
        print 'The school with the best ratio is {}.'.format(BESTSCHOOLRATIO)

    elif data == 'district':
        print 'The district with best ratio is {}.'.format(BESTDISTRICTRATIO)

    else:
        print "Please enter 'school' or 'district'."


def generate_json():
    """This function generates the result dataset as json file.

    Args:
        None.

    Returns:
        File: JSON file

    Examples:
        >>> generate_json()
        Creating combined_data.json file....
        Done.
        """
    print 'Creating combined_data.json file....'
    out_file = open("combined_data.json", "w")
    json.dump(COMBODICT, out_file, indent=4)
    out_file.close()
    print 'Done.'
