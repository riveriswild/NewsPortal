py manage.py makemigrations
py manage.py migrate
py manage.py shell
from news.models import *


#Создать двух пользователей (с помощью метода User.objects.create_user).
u1 = User.objects.create_user(username='Jack')
u2 = User.objects.create_user(username='Jane')

# Создать два объекта модели Author, связанные с пользователями.
Author.objects.create(authorUser=u1)
Author.objects.create(authorUser=u2)
author = Author.objects.get(id=1)
author2 = Author.objects.get(id=2)

# Добавить 4 категории в модель Category.
Category.objects.create(name='World News')
Category.objects.create(name='IT')
Category.objects.create(name='Education')
Category.objects.create(name='Entertainment')

# Добавить 2 статьи и 1 новость.
Post.objects.create(author=author, categoryType='AR', title='New ideas for your education', text='So, blahblahblah, blahblah,blah')
Post.objects.create(author=author2, categoryType='AR', title='New age', text='some text about something')
Post.objects.create(author=author2, categoryType='NW', title='Welcome', text='text about smth')

# Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=3))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=2))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=4))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=1))

# Создать как минимум 4 комментария к разным объектам модели Post(в каждом объекте должен быть как минимум один комментарий).
Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser,text='commenttext1')
Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=2).authorUser,text='commenttext2')
Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=1).authorUser,text='commenttext1-2')
Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=1).authorUser,text='commenttext1-1')

# Применяя функции like() и dislike()к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=1).dislike()
Post.objects.get(id=2).like()
Post.objects.get(id=2).dislike()
Post.objects.get(id=2).dislike()
Post.objects.get(id=3).dislike()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).dislike()
Comment.objects.get(id=3).dislike()
Comment.objects.get(id=3).dislike()
Comment.objects.get(id=3).dislike()
Comment.objects.get(id=3).dislike()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).like()

# Обновить рейтинги пользователей.
author.update_rating()
author2.update_rating()

# Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
a = Author.objects.order_by('-ratingAuthor')[:1]
for i in a:
...    i.ratingAuthor
...    i.authorUser.username

# Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
Post.objects.all().order_by('-rating').values('dateCreation', 'author__authorUser__username', 'rating', 'title')[0]

# Превью лучшего поста - получилось отдельным действием
b = Post.objects.all().order_by('-rating')[0]
b.preview()

# Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
comments=Comment.objects.filter(commentPost = Post.objects.all().order_by('-rating')[0])
comments.values('dateCreation', 'commentUser__username','text', 'rating')