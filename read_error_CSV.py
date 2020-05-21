import csv
import argparse
from jira import JIRA
import subprocess
import argparse
import json
import os
import sys


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file_name", required=True, help='csv file name')
    parser.add_argument("-e", "--error_type", choices=['ANR', 'App_crash', 'Tombstone'], help='error type(ANR,App_crash or tombstone)')
    parser.add_argument("-b", "--build_version", required=True, help='SW version')
    parser.add_argument("-p", "--package_name", help='error app')
    parser.add_argument("-H","--HW_version",choices=['EVT', 'DVT', 'PVT'],default='EVT',help='if not EVT please specify')
    parser.add_argument("-s","--severity",choices=['Critical', 'Serious', 'Moderate'],default='Serious',help='Critical Serious or Moderate')
    parser.add_argument('-v', "--verbose", action='store_true',  default=False,  help='output verbose information if specified')
    return parser.parse_args()

def _main():
    try:
        global verbose_flag
        args = parse_args()
        if args.verbose:
            verbose_flag = True
        success = True
       
    except Exception as e:
        print("e=%s" % e)
    if success:
        title = {
            'ANR':'system_app_anr@',
            'App_crash' : 'system_app_crash@',
            'Tombstone' : 'SYSTEM_TOMBSTONE@'
        }
        auth = open('auth.json')
        info = json.load(auth)
        name = info['user']
        password = info['password']
        jira = JIRA('http://jira.fihbdc.com:8080',basic_auth=( name, password))
        with open(args.file_name,'r') as myFile:
            lines=csv.reader(myFile)
            for line in lines:     #line[3] description,  line[0] error type, line[1] packagename, line[5] logpath
                if line[0] == args.error_type and line[1] == args.package_name:
                   # print('python3 report.py -t [V0.170]' + title[args.error_type] + args.package_name + ' -b V0.170 -p auth.json -d' + line[3] + 'log Path: \n' + line[5])
                    issue_dict= {
                        'project': {'id':'11301'},# <JIRA Project: key='BT1', name='B130DL', id='11301'>
                        'summary': '[MTBF][' + args.build_version +']' + title[args.error_type] + args.package_name,
                        'description': line[3] + 'log Path: \n fihtdc  \n fihtdc' + line[5],
                        'issuetype': {'name': 'SW Bug'},
                        'components':[{'name': 'Stability'}],
                        'customfield_10412': {'value':'Auto-MTBF'},
                        'customfield_10201':[{'id':'10205'}], #value='China/Beijing', id='10205' value='USA', id='10240'
                        'customfield_10501':{'value':'Yes'},  #FIH can reporeduce
                        'customfield_10700':{'value':args.HW_version}, #PVT,EVT or DVT
                        'customfield_10503':{'id':'10816'}, #frequency Occasional(10%-49%)
                        'customfield_10411':{'value':args.severity },#value='Critical', id='10616'  value='Serious', id='10617'
                        'customfield_10202':[{'id':'10311'}],#value='China Unicom', id='10291' value='CMCC', id='10311'
                        'customfield_10400':args.build_version, #SW version
                    }
                    new_issue = jira.create_issue(fields=issue_dict)
                    print(new_issue.key + '  ' + new_issue.summary)
                    break  

if __name__ == '__main__':
    _main()