import unittest
import requests
import json

class Test_JP_Posts_API(unittest.TestCase):

    def test_00_request_returns_success(self):
        r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        self.assertEqual(r.status_code,200)

    def test_01_request_returns_json(self):
        r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        self.assertTrue('application/json' in r.headers['Content-Type'])

    def test_02_request_returns_a_post(self):
        r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        post = json.loads(r.text)
        self.assertTrue(type(post) is dict)
        self.assertEqual(post['id'],1)
        for item in ['title','body','userId']:
            self.assertTrue(item in post)
        self.assertTrue(type(post['title']) is str)
        self.assertTrue(type(post['body']) is str)
        self.assertTrue(type(post['userId']) is int)

    def test_03_request_query_returns_a_list(self):
        r = requests.get("https://jsonplaceholder.typicode.com/posts?id=1")
        posts = json.loads(r.text)
        print(posts)
        self.assertTrue(type(posts) is list)
        self.assertTrue(len(posts) == 1)

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False, warnings='ignore')
