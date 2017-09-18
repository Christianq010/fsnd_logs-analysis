import psycopg2
from datetime import datetime

DB_NAME = "news"


# Create the following Views before executing this file
"""
CREATE VIEW article_views AS
SELECT title,count(log.id) AS views
FROM articles,log
WHERE log.path = CONCAT('/article/', articles.slug)
GROUP BY articles.title
ORDER BY views DESC;

CREATE VIEW authors_by_article AS
SELECT title, name
FROM articles, authors
WHERE articles.author = authors.id;

CREATE VIEW total_status2 AS
SELECT time ::timestamp::date AS day, cast(count(status) AS float) AS total
FROM log
GROUP BY day
ORDER BY total DESC;

CREATE VIEW errors2 AS
SELECT time ::timestamp::date AS day, cast(count(status) AS float) AS errors
FROM log
WHERE status != '200 OK'
GROUP BY day
ORDER BY errors DESC;

"""

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
    query1 = """
            select title, views 
            from article_views limit 3;
            """
    popular_articles = fetch_results(query1)
    print """ The most popular three articles """
    for result in popular_articles:
        print '\n' + '"' + result[0] + '" -- ' + str(result[1]) + " views"
    print(' ')


# Question 2. Who are the most popular article authors of all time?
def print_popular_authors():
    query2 = """
            SELECT name, sum(article_views.views) AS views
            FROM authors_by_article, article_views
            WHERE authors_by_article.title = article_views.title
            GROUP BY name ORDER BY views DESC;
            """
    popular_authors = fetch_results(query2)
    print """ The Most Popular Authors """
    for result in popular_authors:
        print '\n' + '"' + result[0] + '" -- ' + str(result[1]) + " views"
    print(' ')


# Question 3. On which days did more than 1% of requests lead to errors?
def print_error_request():
    query3 = """
            SELECT errors2.day, (errors2.errors/total_status2.total * 100)
            AS Error_Percentage
            FROM errors2, total_status2
            WHERE total_status2.day = errors2.day
            AND (((errors2.errors/total_status2.total) * 100) > 1.0)
            ORDER BY errors2.day;
            """    
    error_log = fetch_results(query3)
    print """ The Most Popular Authors """
    for result in error_log:
        print '\n' + '"' + str(result[0]) + '" -- ' + str(result[1]) + "% errors"
    print(' ')

# Run all 3 functions when executed
if __name__ == "__main__":
    print_popular_articles()
    print_popular_authors()
    print_error_request()
