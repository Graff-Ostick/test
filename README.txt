# Test

Test is a simple MVP. It have a list of news with functionality to upvote and comment on them

## Usage
Download project.
Open cmd and write: path_to_project\test\rest>python manage.py runserver.
Next open any browser and write in url field http://127.0.0.1:8000/api/api to see all rest query
You must see next:
   key - name of actions : value - url link that need to add to "http://127.0.0.1:8000/api/"
            'List': '/task-list/',
            'Detail View': '/task-review/<str:pk>/',
            'Create article': '/task-create/',
            'Update article': '/task-update/<str:pk>/',
            'Delete article': '/task-delete/<str:pk>/',
            ' ': ' ',
            'Review': '/review-check/',
            'Check review by article and id': '/task/<str:pk>/check-comment/<str:pk1>/',
            'Create review': 'review-add/',
            'Update review': 'task/<str:pk>/review-update/<str:pk1>',
            'Delete review': 'task/<str:pk>/review-delete/<str:pk1>',

Also you can open:
    http://127.0.0.1:8000/api/article - check exist articles
    http://127.0.0.1:8000/api/reviews - check exist reviews

Functionality to add comment and review in page "/article" and "/reviews" will be added to 24.06.2020 23:00

```python

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

