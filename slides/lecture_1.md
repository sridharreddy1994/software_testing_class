# Software Testing Methodology

## Gregory S. DeLozier Ph.D.
## Fall 2016

# Lecture 1
---
# Contact Information

Gregory S. DeLozier Ph.D.

gdelozie@kent.edu

github.com/gregdelozier/software_testing_class

---
# In Scope

- Explore the purpose of testing software
- Learn about the varieties of testing
- Learn some testing strategies
- Get experience with specific testing tools
- Test an entire, significant app front-to-back
- Explore the current testing research

--- 
# Also In Scope

- Refresh (or learn) some basic supporting skills
    - Web skills
    - Python
    - Cloud services
    - Building a portfolio

---
# Out of Scope

- Basic programming
- Simple SQL skills
- Chasing after missing homework
- Expensive textbooks

---
# Class Project

- There is no class project
- Trust me, you'll have enough to do

---
# Grading

- Weekly homework. Do this.   20%
- Midterm.  20%
- Getting the application done and tested.  20%
- Final exam. In class, open handwritten notes.  40%

---
# Policies – Missing Things

- Missing class is not good. If you miss a lecture or a lab exercise, you will have to get that information and experience somewhere.
- On weekly assignments, there are no makeups. Some grading is automated, and I will discuss the assignments the following week. Get them done.
- On other assignments, except the final, if you are having trouble with a date, see me.

---
# Policies – Class Conduct

- The usual rules about adult behavior apply.
- Kent is serious about academic honesty.
- Keep the laptop and phone distraction to a minimum when we’re doing things together.
- I have no problem with snacks and drinks, and I will check on Kent’s rules. This is a nice room, and was just remodeled, so keep it clean.
- We will have two breaks. If you need to leave between breaks, be discreet, please.

---
# Policies – Extreme Circumstances

- If something unusual is happening at the university, we might not have class if the university is closed.
- If something unusual happens to me, and I’m not here by 7:30, we won’t have class.
- If either one of these happens, adjusted homework and lecture notes will be posted on the web within 24 hours. You will still be responsible for getting assignments done.

---
# Skills You Will Need

- Programming basics
- How to use an IDE, how to debug
- Basic language skills
    - SQL
    - Python
    - Javascript
- Know your way around a Linux command line
- Some idea of how the web works
- Some way to write scientific English

---
# Stuff You Need to Get

- A reasonable computer
    - Windows, Mac, Linux
    - Chrome, Firefox
- Possibly some free software (Python, Mongo, etc.)
- A solid web connection
- Something to keep a lot of information safe
    - (i.e. a notebook, a document, etc.)
    - You will be storing passwords

---
# Stuff You Need to Sign Up For

- An account at PythonAnywhere 
    - (the $5 version is fine)
- Various internet free services
    - TravisCI
    - UptimeRobot
    - Etc

---
# Stuff You Need to Read

- Open source books as assigned
- Various system documentation
- On-line articles and industry commentary
- Research papers regarding database topics

---
# BREAK TIME :-)
---
# We Test To Get Error-Free Software
---
# We Test To Get Error-Free Software (?)
---
# Demo Time
---
# Purpose of Testing?

- To get evidence of value to someone

- Unless you can bound the universe, you can't prove correctness

- You can get a lot of evidence, though

---
# What is Value?

- Potential Benefit
    - Presumably does something useful

- Components of Benefit
    - Probability of success * benefit of success
    - Probability of failure * cost of failure

- Think of some examples

---
# Value Proposition

- When is a thing viable? 

- When is a thing optimal?

---
# How to Increase Value?

- Increase probability of success

- Increase value of success 
    - (not really a testing problem)

- Decrease probability of failure

- Decrease the cost of failure

---
# Increasing Probability of Success

- Test things that must work 
    - Much more on this later

---
# Decreasing Probability of Failure

- Test success
- Explore unexpected areas
- Test a _lot_

---
# Decreasing Cost of Failure

- Bound failure (that's a design issue

- Fail in controlled, low-cost ways
    - Quite a bit more on this later, too

---
# Keep your Purpose in Mind

- What are you trying to accomplish?

- Who gets the value, and what is is?

- When is enough evidence gathered?

---
# Testing Frameworks - An Intro

- We will use python's _unittest_ framework
- Read about it here:
    - https://docs.python.org/3/library/unittest.html
- _import unittest_


---
# Example Code

    !python
    
    def upper(s):
      ...
      # return a string
        
    def isupper(s):
      ...
      # return a boolean

---
# Example Test

    !python
    import unittest
    
    class TestStringMethods(unittest.TestCase):
    
      def test_upper(self):
          self.assertEqual('foo'.upper(), 'FOO')

      def test_isupper(self):
          self.assertTrue('FOO'.isupper())
          self.assertFalse('Foo'.isupper())
    
    if __name__ == '__main__':
        unittest.main()
---
# DEMO TIME
---

