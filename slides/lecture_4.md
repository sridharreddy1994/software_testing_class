# Database Layer Testing
## Lecture 4
## Software Testing Methodology

---

# Agenda

1. Administrative stuff

1. TDD Wrap-Up

1. What to test with DBMS?

1. How to test the DBMS?

---

# Administrative Stuff

1. Blackboard is fixed.

1. Homework to follow.

1. Today's code will be posted on GitHub

    - Details in the homework
  
1. I have to do the _Academic Presence Verification_

    - That means you have to submit an assignment 
    - _Before Friday_
    - _Any assignment_

---

# TDD Wrap-Up

* Tests can be used to develop anything

* Use a simple test framework

* Spend time on the connection method

    UI  - WebDriver
    API - Requests
    ...etc

---

# Demo Time

---

# What to test with DBMS?

* Presence
* Structure
* Behavior
* Interaction

---

# Presence

     * Connection
     * Persistence
     * Networking

---

# Structure

     * Tables
     * Columns
     * Index/Keys
     * Users

---

# Behavior

* Are constraints in place?
    * Data Types
    * Relationships

* Does active code work?
    * Stored procedures
    * Triggers

* Does authentication work?
    * Access allowed
    * Access (or write) denied

---

# Interaction

* Is the correct data being stored
    * Balancing results

* Is the data returned what is expected
    * Preview expectations

* Is the performance adequate
    * Overall time
    * Reliability
    * Variation

---

# Black Box Testing

* Testing from the outside

* Safer

* Easier to set up

* Remote testing

---

# White Box Testing

* Looking inside

* More ability to test

* Requires access to internals

* Requires authority

---

# Testing Stages

* Clean up data
* Set up initial data
* Test run
* Outcome verification
* Tear down

__Looks a lot like TDD__

---

# Difficulties and Problems

* Expensive

* Constantly changing

* Dangerous to look at real data

* Difficult to get test data

* Slow - many tests take time to run

---

# When to test

* During development - TDD

* During acceptance testing

* During regression testing

---

# How to test the DBMS?

* Database Browser
    * SQLite Browser

* Programming Interface
    * Sqlite3 package

* API Testing & Balancing
    * Requests

* UI Testing & Balancing
    * WebDriver

---

# Demo Time

---

# Resources

* http://www.agiledata.org/essays/databaseTesting.html
* https://en.wikipedia.org/wiki/Database_testing
* http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
