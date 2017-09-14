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
  The database includes three tables:
  * The authors table includes information about the authors of articles.
  * The articles table includes the articles themselves.
  * The log table includes one entry for each time a user has accessed the site.