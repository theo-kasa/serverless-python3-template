import json
import requests


def handler(event, context):
    your_ip = requests.get('https://httpbin.org/ip').json()['origin']
    response = {
        'statusCode': 200,
        'body': json.dumps({'myIp': your_ip})
    }

    return response
