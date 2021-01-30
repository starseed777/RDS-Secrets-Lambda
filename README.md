This python code connects to an AWS RDS database, passing in the database credentials from AWS Secrets Manager.
After connecting to the database we are able to inject data into the database by writing the mysql injection (passed in query and region also as a secret outside of secrets manager just for best security practices as well).
