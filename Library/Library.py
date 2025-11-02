class Library():

    max_borrow_days = 14

    def __init__(self,books = dict,user = dict):

        self.book = books
        self.user = user


    def register_user(self,user):

