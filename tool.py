import psycopg2
DB_NAME = "news"



# Connect to our Database and Fetch_Results
def fetch_results(query):
    try: 
        # Connect to our Database
        db = psycopg2.connect(database=DB_NAME)
        # cursor runs queries and fetches results
        c = db.cursor()
        # execute queries above from the cursor 
        c.execute(query)
        # fetch results from the cursor
        query_results = c.fetchall()
        db.close()
        return query_results
    except BaseException:
        print ("Sorry, unable to fetch results from Database")

# Question 1. What are the most popular three articles of all time?
def print_popular_articles():
    # Query for Top 3 results
    query1 = """
            select title,count(log.id) as views 
            from articles,log 
            where log.path = CONCAT('/article/', articles.slug) 
            group by articles.title 
            order by views desc limit 3;
            """
    popular_articles = fetch_results(query1)
    print """ The most popular three articles """
    for result in popular_articles:
        print '\n' + '"' + result[0] + '" -- ' + str(result[1]) + " views"
    print(' ')


# Question 2. Who are the most popular article authors of all time?
# def print_popular_authors():
    

# Question 3. On which days did more than 1% of requests lead to errors?
# def print_error_request():
    





print_popular_articles()

