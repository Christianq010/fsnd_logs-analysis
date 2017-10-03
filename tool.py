#! /usr/bin/env python

import psycopg2
from datetime import datetime


# Create the Views as instructed on the README file first

# Question 1. What are the most popular three articles of all time?
def print_popular_articles():
    print " The Most Popular Articles "
    print '--'
    query1 = """
            select title, concat(concat(page_views,' '), 'views')as views
            from top_3_articles limit 3;
            """
    try:
        # Connect to our Database
        database = psycopg2.connect(database="news")
        # cursor runs queries and fetches results
        c = database.cursor()
        # execute queries above from the cursor
        c.execute(query1)
        # fetch results from the cursor
        query_results = c.fetchall()
        database.close()
        # Iterate over the rows and get our results
        for i in query_results:
            print('"' + i[0] + '"' + ' -- ' + i[1])
        print '\n'
    except BaseException:
        print("Sorry, unable to fetch results from Database")


# Question 2. Who are the most popular article authors of all time?
def print_popular_authors():
    print " The Most Popular Authors "
    print '--'
    query2 = """
            select name, concat(concat(page_views,' '), 'views')as views
            from top_authors join authors on top_authors.author = authors.id
            limit 4;
            """
    try:
        database = psycopg2.connect(database="news")
        c = database.cursor()
        c.execute(query2)
        query_results = c.fetchall()
        database.close()
        for i in query_results:
            print('"' + i[0] + '"' + ' -- ' + i[1])
        print '\n'
    except BaseException:
        print("Sorry, unable to fetch results from Database")


# Question 3. On which days did more than 1% of requests lead to errors?
def print_error_request():
    print " Days in which more than 1% of requests lead to errors "
    print '--'
    query3 = """
            select date, concat(concat(daily_error_percentage,'%'), ' errors')
            as percentage
            from daily_error_percentage_table limit 1;
            """
    try:
        database = psycopg2.connect(database="news")
        c = database.cursor()
        c.execute(query3)
        query_results = c.fetchall()
        database.close()
        for i in query_results:
            print(i[0].strftime('%B %d, %Y') + ' -- ' + i[1])
        print '\n'
    except BaseException:
        print("Sorry, unable to fetch results from Database")


# Run all 3 functions when executed
if __name__ == "__main__":
    print_popular_articles()
    print_popular_authors()
    print_error_request()
