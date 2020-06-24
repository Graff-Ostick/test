from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('article/', views.showArticle, name="article"),
    path('reviews/', views.showComment, name="review"),
    path('article/<int:pk>', views.AddUpvote.as_view(), name='add-upvotes'),
    path('reviews/<int:pk>', views.showCurrentCommet, name='add-comment'),

    path('api', views.apiView, name="api-view"),
    path('task-list/', views.ArticleList, name="task-list"),
    path('task-review/<str:pk>', views.ArticleReview, name="task-review"),
    path('task-create/', views.ArticleCreate, name="task-create"),
    path('task-update/<str:pk>', views.ArticleUpdate, name="task-update"),
    path('task-delete/<str:pk>', views.ArticleDelete, name="task-delete"),

    path('review-check', views.CheckAllReview, name="review-check-comment"),
    path('task/<str:pk>/check-comment/<str:pk1>', views.CheckArticleReview, name="review-check-comment"),
    path('review-add', views.AddReview, name="task-add-comment"),
    path('task/<str:pk>/review-update/<str:pk1>', views.UpdateReview, name="task-update-comment"),
    path('task/<str:pk>/review-delete/<str:pk1>', views.DeleteReview, name="task-delete-comment"),
]
