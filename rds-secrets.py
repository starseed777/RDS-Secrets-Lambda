import boto3

import json 

import mysql.connector

from secrets import region, inject, injectvalue 

client = boto3.client('secretsmanager', region_name = region)

response = client.get_secret_value(
    SecretId="stage/deloitte/mysql"
)

secretparse = json.loads(response["SecretString"])


mydb = mysql.connector.connect(
    host = secretparse["host"],
    user = secretparse["username"],
    passwd = secretparse["password"],
    database = secretparse["dbInstanceIdentifier"]
)

mycursor = mydb.cursor()

sql = inject 
value = injectvalue 
mycursor.execute(sql,value)

mydb.commit()

print(mycursor.rowcount, "Record inserted")
