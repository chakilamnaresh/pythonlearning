import cx_Oracle
conn=cx_Oracle.connect("naresh","nakannaya","localhost:1521/xe")
if(conn):
    print("connection is successfull")
else:
    print("connection is not successful")

cursor=conn.cursor()
cursor.execute(
    """Select * from Products""")
for results in cursor:
    print("Product ID:",results)



