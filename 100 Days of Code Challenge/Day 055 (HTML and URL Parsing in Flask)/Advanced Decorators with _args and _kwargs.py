class User:
    """User class"""
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    """decorator to check if user is logged in"""
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    """enable user to create blog"""
    print(f"This is {user.name}'s new blog post.")


new_user = User("Ernest")
new_user.is_logged_in = True
create_blog_post(new_user)
