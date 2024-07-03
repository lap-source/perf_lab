#!/usr/bin/env python3

import sys
import os
import json
from collections import OrderedDict


def json_load(file):
    with open(file, 'r') as f:
        return json.load(f, object_pairs_hook=OrderedDict)


def json_write(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=2)


def merge_tests_values(vals, tests):
    for test in tests:
        if test['id'] in vals:
            test['value'] = vals.get(test['id'])
        if 'values' in test:
            merge_tests_values(vals, test['values'])


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 %s <file_values> <file_tests> <file_report>" % os.path.basename(sys.argv[0]))
        sys.exit(0)

    file_values = sys.argv[1]
    file_tests = sys.argv[2]
    file_report = sys.argv[3]

    values_json = json_load(file_values)
    tests_json = json_load(file_tests)

    values = {value['id']: value['value'] for value in values_json['values']}
    merge_tests_values(values, tests_json['tests'])

    json_write(file_report, tests_json)
