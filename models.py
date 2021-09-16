import json
from os import waitpid

from wtforms.compat import with_metaclass

class Posts:
    def __init__(self):
        try:
            with open("posts.json", "r") as f:
                self.posts = json.load(f)
        except FileExistsError:
            self.posts = []

    def all(self):
        return self.posts
    
    def get(self, id):
        return self.posts[id]

    def create(self, data):
        data.pop('csrf_token')
        self.posts.append(data)

    def save_all(self):
        with open('posts.json', "w") as f:
            json.dump(self.posts, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.posts[id] = data
        self.save_all()

posts = Posts()