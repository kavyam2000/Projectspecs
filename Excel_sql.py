import mysql.connector as mysql
from datetime import date
import boto3 as boto3
import csv as csv

client = boto3.client("s3")
try:

 print ( "Start of the program")
 bucket_name = 'firstbucket-kkt'
 s3_file_name = 'newproducts1.csv'
 res = client.get_object(Bucket=bucket_name, Key=s3_file_name)
    #download_path = '/home/ubuntu/db/'.format(s3_file_name)
 download_path = '/tmp/{}{}'.format(uuid.uuid4(), s3_file_name)
 client.download_file(bucket_name,s3_file_name,download_path)
 csv_data = csv.reader(download_path)
 print ( "End of S3 download")

 cnx = mysql.connect(user='kavyamark', password='kavyamark24',
         host='terratest-example.ct9w3ysjragu.us-east-2.rds.amazonaws.com',
                              database='TestDB',
                              use_pure=False)
cursor = cnx.cursor()

 print ( "After DB connect")
 today = date.today()

 ifh = open(download_path, 'r')
 csv_data = csv.reader(ifh, delimiter=',')
 #print (csv_data)
 for row in csv_data:
    cursor.bindarraysize = 1
    cursor.setinputsizes(int, 20, float)
    print("insert from excel")
    print(row)
    cursor.execute('insert into products (item_no, item_name, description, active, createdate) VALUES(:1, :2, :3,today)', row)
    print("AF insert")


 #add_prod = ("INSERT INTO products "
  #             "(item_no, item_name, description, active, createdate) "
   #            "VALUES (%s, %s, %s, %s, %s)")

#data_prod = ('K5431', 'Shirt', 'Longsleevesweater','1',today)

# Insert new product

 print ( "After cursor")
# Now execute the sqlquery
 #cursor.execute(add_prod, data_prod)
 #item_no = cursor.lastrowid

# Make sure data is committed to the database
 cnx.commit()


except mysql.Error as e:
    print("There is a problem with mysql", e)

# by writing finally if any error occurs
# then also we can close the all database operation
finally:
    if cursor:
        cursor.close()
    if cnx:
        cnx.close()
