import psycopg2
DB_NAME = "news"

# Question 1. What are the most popular three articles of all time?
query1 = """ .. """

# Question 2. Who are the most popular article authors of all time?
query2 = """ ... """

# Question 3. On which days did more than 1% of requests lead to errors?
query3 = " ..  "

# Connect to our Database
db = psycopg2.connect(database=DB_NAME)

# cursor runs queries and fetches results
c = db.cursor()

# execute queries above from the cursor 
c.execute(query1)

# fetch results from the cursor
results = c.fetchall()

db.close()
