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
Create view top_authors4 as
select author, count(*) as page_views
from articles join log
on log.path = concat('/article/', articles.slug)
where status !='404 NOT FOUND'
group by articles.author 
order by page_views desc;
```


#### The Python Reporting Tool 
  * After the Views have been created, inside the virtual machine run `tool.py` with - 
  ```python
  python tool.py
  ```
  * The python file `tool.py` executes 3 functions, printing out the answers onto the terminal.

#### Notes: 
  * Use ES Lint to Clean Code to PEP Standards.

### References
* https://www.postgresql.org/docs/9.5/static/functions-string.html
* http://initd.org/psycopg/docs/usage.html
* https://stackoverflow.com/questions/770579/how-to-calculate-percentage-with-a-sql-statement
* https://stackoverflow.com/questions/466345/converting-string-into-datetime
* https://www.postgresql.org/message-id/42231EB6.9F6D20F3%40rodos.fzk.de
* http://www.zentut.com/sql-tutorial/sql-inner-join/