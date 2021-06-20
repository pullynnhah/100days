class User:
    def __init__(self, name):
        self.name = name
        self.is_log_in = False


def authentication_decorator(func):
    def wrapper(*args, **kwargs):
        if args[0].is_log_in:
            func(args[0])
        else:
            print("Please LOGIN before trying to act!")

    return wrapper


@authentication_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("angela")
create_blog_post(new_user)

new_user.is_log_in = True
create_blog_post(new_user)
