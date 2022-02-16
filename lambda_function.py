import boto3
import os
from boto3.dynamodb.conditions import Key

DYNAMO_BD = os.environ['DYNAMO_BD']

# Hola a todos estoy con RedHat y los companeritos
# Modificacion ED, Wed Feb 16 00:00:55 -05 2022

class DynamoAccessor:
    def __init__(self, dynamo_table):
        dynamo_db = boto3.resource('dynamodb')
        self.table = dynamo_db.Table(dynamo_table)

    def get_data_from_dynamo(self, CC):
        response = self.table.query(KeyConditionExpression=Key('CC').eq(CC))
        return response["Items"][0] if any(response["Items"]) else None

def lambda_handler(event, context):
    dynamo_backend = DynamoAccessor(DYNAMO_BD)
    db_element = dynamo_backend.get_data_from_dynamo(event['CC'])
    return db_element

