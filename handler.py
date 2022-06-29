import json
from random import random

import boto3

SFN = boto3.client('stepfunctions')
SQS = boto3.client('sqs')


def creditCheck(event, context):
    print(event)

    #Simulate processing of cretid Check
    return event


def wallet(event, context):
    print(f'# event={json.dumps(event)}')
    body = json.loads(event['Records'][0]['body'])

    print(f'# {body}')

    change = random()

    if change < 0.7 : 
        SFN.send_task_success(
                taskToken=body['taskToken'],
                output=json.dumps({ 
                    'msg': 'this goes to the next state',
                    'credit_status': True 
                }))
    else:
        SFN.send_task_success(
                taskToken=body['taskToken'],
                output=json.dumps({ 
                    'msg': 'this goes to the next state',
                    'credit_status': False 
                }))