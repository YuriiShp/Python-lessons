import datetime


class User:

    def __init__(self, name, last_name, interest):
        self.name = name
        self.lastname = last_name
        self.interest = interest
        self.blog = None

    def create_blog(self):
        blog_title = self.interest + ' by ' + self.name + ' ' + self.lastname
        self.blog = Blog(blog_title)

    def add_post(self, text):
        post = Post(text)
        self.blog.add(post)


class Blog:

    def __init__(self, title):
        self.title = title
        self.posts = []

    def add(self, post):
        post.author = self.title
        self.posts.insert(0, post)


class Post:

    def __init__(self, text):
        self.author = None
        self.text = text
        self.date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        self.likes = 0
        self.replies = []

    def read(self):
        print(f'from {self.author} \n'
              f'{self.date} \n'
              f'{self.text} \n'
              f'Likes: {self.likes}        Replies: {len(self.replies)}')

    def like(self):
        self.likes += 1

    def reply(self, user, text):
        message = user.name + ' ' + user.lastname + ': ' + text
        self.replies.append(message)

    def __repr__(self):
        return self.date


class Feed:

    def __init__(self, user_list):
        self.posts = []
        self.user_list = user_list

    def read(self):
        for user in self.user_list:
            self.posts.extend(user.blog.posts)

        # self.posts.sort(key=lambda date: datetime.datetime.strptime(date, "%d/%m/%Y %H:%M")) #Сортування по даті

        for post in self.posts:
            post.read()
