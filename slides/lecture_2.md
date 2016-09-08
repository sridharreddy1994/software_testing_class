# Software Testing Methodology

## Gregory S. DeLozier Ph.D.
## Fall 2016

# Lecture 2
---
# Testing Layers
---
# Technology Stacks

- Where does an application exist? 
- We think of application layers.

--- 
# GUI Layer

- This is the Layer where the user interacts
- Implements the user interface
- This is normally where people test

---
# Web API Layer

- Application network requests
- Implements communication
- Possibly AJAX (from browser)
- Possibly WebAPI (from another system)
- "REST" API

---
# Module API Layer

- Libraries of code
- Externally exposed interfaces
- Implement business rules

---
# Class Method/Function Layer

- Individual functions
- Implement business operations
- Usual place to base TDD

---
# Security Layer

- Implement permissions
- Challenging to test
- Expensive to fail

---
# Database/Storage Layer

- Implement storage
- Implement schema/relationships
- Not common, but useful to test

---
# Enviromental Layer

- Implements application dependencies
- CI and regression testing
- Causes a lot of production failures

---
# Infrastructure Layer

- Divides into sublayers
    - networks
    - server
    - balancer,etc.

- Emerging as test target

---
# Testing Frameworks - Review

- We will use python's _unittest_ framework
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
# Tools for Layers

- GIU - Webdriver
- API - Requests
- Module/Class/Function - direct call
- Security - libraries
- Database - data drivers/ORMs
- Enviroment - configuration libraries
- Infrastructure - configuration tools, ad hoc

---
# WebDriver

- This is a programmable robot for GUIs

- Documentation is here:

    http://selenium-python.readthedocs.io

---
# Requests

- This is a programmable way to sent HTTP requests

- Documentation is here:

    http://docs.python-requests.org/en/master/

---
# Demo Time 
---


