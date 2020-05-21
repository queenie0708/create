from jira import JIRA
import subprocess
import argparse
import json
import os
import sys

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--title", required=True, help='bug title')
    parser.add_argument("-d", "--description", required=True, help='bug content')
    parser.add_argument("-b", "--build_version", required=True, help='SW version')
    parser.add_argument("-a", "--attachment_path",required=False,help='path of attachment file')
    parser.add_argument("-p", "--auth_path", required=True, help='path of attachment file')
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
        auth_path = args.auth_path

    except Exception as e:
        print("e=%s" % e)
    if success:
        auth = open(auth_path)
        info = json.load(auth)
        name = info['user']
        password = info['password']
        #print( name,password)
        jira = JIRA('http://jira.fihbdc.com:8080',basic_auth=( name, password))
        issue_dict= {
            'project': {'id':'11301'},# <JIRA Project: key='BT1', name='B130DL', id='11301'>
            'summary': args.title,
            'description': args.description,
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
        # 'attachment':r'/mnt/d/MTBF/BT1/0.096/testTC90BluetoothTethering_20200406_020504.zip'  
        }
        new_issue = jira.create_issue(fields=issue_dict)
        if args.attachment_path:
            jira.add_attachment(issue=new_issue, attachment=args.attachment_path)
        print(new_issue.key)
if __name__ == '__main__':
    _main()