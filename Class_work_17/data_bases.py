import mongoengine.fields
import pymongo
from mongoengine import *

connect('pupils')

class User(Document):
    enter_date = mongoengine.fields.DateField()
    School_N = StringField
    first_name = StringField(max_length=20, required=True)
    last_name = StringField(max_length=20, required=True)
    average_mark = StringField(max_length=20, required=True)

#
ross = User(email='invanov.vas@google.com', first_name='Ivanovich', last_name='Vasil').save()
#
# class Post(Document):
#     title = StringField(max_length=100, required=True)
#     author = ReferenceField(User)
#
#     meta = {'allow_inheritance': True}
#
# class TextPost(Post):
#     content = StringField()
#
# class ImagePost(Post):
#     image_path = StringField()
#
# class LinkPost(Post):
#     link_url = StringField()
#
# class Post(Document):
#     title = StringField(max_length=120, required=True)
#     author = ReferenceField(User)
#     tags = ListField(StringField(max_length=30))
#
# class Comment(EmbeddedDocument):
#     content = StringField()
#     name = StringField(max_length=120)
#
# class Post(Document):
#     title = StringField(max_length=120, required=True)
#     author = ReferenceField(User)
#     tags = ListField(StringField(max_length=30))
#     comments = ListField(EmbeddedDocumentField(Comment))
#
# class Post(Document):
#     title = StringField(max_length=120, required=True)
#     author = ReferenceField(User, reverse_delete_rule=CASCADE)
#     tags = ListField(StringField(max_length=30))
#     comments = ListField(EmbeddedDocumentField(Comment))
#
# post1 = TextPost(title='Fun with MongoEngine', author="john")
# post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
# post1.tags = ['mongodb', 'mongoengine']
# post1.save()
#
# post2 = LinkPost(title='MongoEngine Documentation', author="ross")
# post2.link_url = 'http://docs.mongoengine.com/'
# post2.tags = ['mongoengine']
# post2.save()