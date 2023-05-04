# PROJECT-DIPLOM

DIPLOM PROJECT

of Python 23 IT Step University

Yurij-Bielousov Сайт поиска помогаек
    Работа над ошибками:
В первой версии:
- сайт только на английском языке, но с при целом на перевод на 7 языков(версия 2).
Планы на 2 версию:
- Модифицировать чат-Бот.
- добавить фичи: 
- разделить отзывы на статьи и события, новые модели:

class Review_Article(Review):
    article_title = models.CharField(max_length=255)
    article_author = models.CharField(max_length=255)

    class Meta:
        unique_together = (("article_title", "article_author", "reviewer_name"),)


class Review_Event(Review):
    event_title = models.CharField(max_length=255)
    event_location = models.CharField(max_length=255)

    class Meta:
        unique_together = (("event_title", "event_location", "reviewer_name"),)
соответствующим образом модернизировать модерицию и т.д. ...

Извлеченные уроки:
- не косячить с именами шаблонов, форм и урлов, сразу создавать таблицу "Связи в проекте" проектировать и вести Имена в ней
- надо разделить каждую страницу на отдельное приложение(views.py на 600 строк не устраивает)