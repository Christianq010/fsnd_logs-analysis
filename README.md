# Log-Analysis

### Project Description
>You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

>The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

### Getting Started

#### PreRequisite Installations:
  * The Virtual Machine - [Vagrant](https://www.vagrantup.com/)
  * [Python3](https://www.python.org/)

#### Run Project:
  1. Download or Clone the following [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) and place into a desired folder on your local machine.
  2. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip and place the file `newsdata.sql` into the directory containing the files above. 
  3. Start and successfully log into the the Linux-based virtual machine (VM) in the folder containing the Vagrant file with the instructions below.
  
#### Launching the Virtual Machine:
  1. Start the Vagrant VM inside Vagrant sub-directory in the `fullstack-nanodegree-vm` repository with:
  
  ```
    $ vagrant up
  ```
  2. Log in with:
  
  ```
    $ vagrant ssh
  ```
  3. Go to relevant directory `cd /vagrant` and `ls`.
  
#### Download the data and Create Views:

  1. Load the data in local database using the command:
  
  ```
    psql -d news -f newsdata.sql
  ```
  * Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
    * `psql` — the PostgreSQL command line program
    * `-d news` — connect to the database named news which has been set up for you
    * `-f newsdata.sql` — run the SQL statements in the file `newsdata.sql`
  
  The database includes three tables:
  * The authors table includes information about the authors of articles.
  * The articles table includes the articles themselves.
  * The log table includes one entry for each time a user has accessed the site.

  2. Use the following commands to explore the database - `psql -d news`.
  * `\dt` — display tables — lists the tables that are available in the database.
  * `\d table` — (replace table with the name of a table) — shows the database schema for that particular table.
  * Drop table even if other tables depend on it  - `DROP TABLE tableName CASCADE;`
  * Use a combination of `select, from and where` SQL statements to explore data, look for connections and draw conclusions.
  
  3. Create the following Views - 
  ```sql
Create view top_3_articles as
select title, count(*) as page_views
from articles join log
on log.path = concat('/article/', articles.slug)
where status !='404 NOT FOUND'
group by articles.title
order by page_views desc;
  ```
  ```sql 
Create view top_authors as
select author, count(*) as page_views
from articles join log
on log.path = concat('/article/', articles.slug)
where status !='404 NOT FOUND'
group by articles.author 
order by page_views desc;
  ```
  ```sql
Create view All_Requests2 as
select time ::timestamp::date as date, count(*) as total_requests
from log
group by date
order by total_requests desc;
  ```
  ```sql
Create view All_Errors2 as
select time ::timestamp::date as date, count(*) as requests_failures
from log
where status = '404 NOT FOUND'
group by date
order by requests_failures desc;
  ```
  ```sql
Create view daily_error_number2 as
select All_Errors2.date,
cast(All_Errors2.requests_failures as decimal) / cast(All_Requests2.total_requests as decimal) as daily_error
from All_Requests2 join All_Errors2
on All_Requests2.date = All_Errors2.date
order by daily_error desc;
  ```
  ```sql
Create view daily_error_percentage_table as
select date,
round(100 * (daily_error), 2) as daily_error_percentage
from daily_error_number2
order by daily_error_percentage desc limit 5;
  ```

#### The Python Reporting Tool 
  * After the Views have been created, inside the virtual machine run `tool.py` with - 
  ```python
  python tool.py
  ```
  * The python file `tool.py` executes 3 functions, printing out the answers onto the terminal.

#### Notes: 
  * Exploring the database in the terminal we find slug in the articles table resemble the path in the log table.
  * We use the concat function and combine '/article/' into the slug to perform a join on the table.
    https://www.w3resource.com/PostgreSQL/concat-function.php
  * The view for our 2nd query is similar to the first but this time we return a table with the author to perform a join with the authors table(id).
  * The idea behind these views, is that we create separate tables for total requests, total errors
  * Then we divide the total errors by total requests
  * I convert it's type to decimal as I ran into errors while rounding up and multiplying in the next table.
    https://stackoverflow.com/questions/42149496/pgsql-error-you-might-need-to-add-explicit-type-casts
  * We cast our timestamp to a date by suffixing it with ::date
    https://stackoverflow.com/questions/6133107/extract-date-yyyy-mm-dd-from-a-timestamp-in-postgresql
  * Used strftime = "string format time" for datetime conversion because I ran into an error printing the query results onto the terminal.
    https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
    http://strftime.org/
  * Use ES Lint to Clean Code to PEP Standards.
    http://pep8online.com/


### References
* https://www.postgresql.org/docs/8.1/static/functions-math.html
* http://initd.org/psycopg/docs/usage.html
* https://stackoverflow.com/questions/770579/how-to-calculate-percentage-with-a-sql-statement
* https://stackoverflow.com/questions/466345/converting-string-into-datetime
* https://www.postgresql.org/message-id/42231EB6.9F6D20F3%40rodos.fzk.de
* http://www.zentut.com/sql-tutorial/sql-inner-join/
* https://stackoverflow.com/questions/6133107/extract-date-yyyy-mm-dd-from-a-timestamp-in-postgresql