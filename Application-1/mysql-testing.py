import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

seek_cur = con.cursor()

query = seek_cur.execute("SELECT * FROM Dictionary")
results = seek_cur.fetchall()

print(results)