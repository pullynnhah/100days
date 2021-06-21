class Post:
    def __init__(self, data):
        self.id = data['id']
        self.body = data['body']
        self.title = data['title']
        self.subtitle = data['subtitle']
