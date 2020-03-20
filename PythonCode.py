import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', aws_access_key_id='AKIARCIYIY7MEFKWKZE6',
				aws_secret_access_key='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',
				region_name='us-east-2')
table = dynamodb.Table('Music')

response = table.scan()

items = response['Items']
print(items)


