# week7-5

class Book:
    def __init__(self, author, publish):
        self.author = author
        self.publish = publish

    def getAuthorInfo(self):
        string = '저자:%s' % self.author
        return string

    def getPublishInfo(self):
        string = '출판사:%s' % self.publish
        return string


class Ebook(Book):
    def __init__(self, author, publish, type):
        super().__init__(author, publish)
        self.type = type

    def getTypeInfo(self):
        string = '유형:%s' % self.type
        return string


book1 = Ebook('파이썬', '00출판사', 'PDF')

print(book1.getAuthorInfo())
print(book1.getPublishInfo())
print(book1.getTypeInfo())
