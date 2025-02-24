import boto3
import psycopg2
import psycopg2.extras
from time import sleep
import json
from datetime import datetime
import os

def convert_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    else:
        return str(obj)

def lambda_handler(event, context):
    print(event)

    def steampipe_query_handler(event):
        # Extracting the SQL query
        query = event['requestBody']['content']['application/json']['properties'][0]['value']

        print("the received QUERY:", query)
        result = execute_steampipe_query(query)
        return result

    def execute_steampipe_query(query):
        # Initialize the Postgres client
        conn = psycopg2.connect(
            database="steampipe",
            host=os.environ.get('HOST_IP'),
            user="steampipe",
            password=os.environ.get('STEAMPIPE_PSD'),
            port="9193"
        )

        try:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute(query)
            data = cursor.fetchall()

            # Convert datetime object
            data = [convert_datetime(val) for val in data]
            return data

        finally:
            cursor.close()
            conn.close()

    action_group = event.get('actionGroup')
    api_path = event.get('apiPath')

    print("api_path: ", api_path)

    result = ''
    response_code = 200

    if api_path == '/execute-steampipe-query':
        result = steampipe_query_handler(event)
    else:
        response_code = 404
        result = {"error": f"Unrecognized api path: {action_group}::{api_path}"}

    response_body = {
        'application/json': {
            'body': result
        }
    }

    action_response = {
        'actionGroup': action_group,
        'apiPath': api_path,
        'httpMethod': event.get('httpMethod'),
        'httpStatusCode': response_code,
        'responseBody': response_body
    }

    api_response = {'messageVersion': '1.0', 'response': action_response}
    return api_response
