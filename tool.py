import psycopg2


# Connect to our Database and Fetch_Results
def fetch_results(query):
    try:
        # Connect to our Database
        db = psycopg2.connect(database="news")
        # cursor runs queries and fetches results
        c = db.cursor()
        # execute queries above from the cursor
        c.execute(query)
        # fetch results from the cursor
        query_results = c.fetchall()
        db.close()
        return query_results
    except BaseException:
        print("Sorry, unable to fetch results from Database")


# Question 1. What are the most popular three articles of all time?
def print_popular_articles():
    print """ The Most Popular Articles """


# Question 2. Who are the most popular article authors of all time?
def print_popular_authors():
    print """ The Most Popular Authors """


# Question 3. On which days did more than 1% of requests lead to errors?
def print_error_request():
    print """ Days in which more than 1% of requests lead to errors """



# Run all 3 functions when executed
if __name__ == "__main__":
    print_popular_articles()
    print_popular_authors()
    print_error_request()
