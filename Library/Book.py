class Book():

    def __init__(self,title,author,isdn,is_available = True):

        self.title = title
        self.author = author
        self.isdn = isdn
        self.is_available = is_available


    def __str__(self):
        return f" name book: {self.title} \n name write: {self.author} \n book id: {self.isdn} \n is available: {self.is_available}"












































































