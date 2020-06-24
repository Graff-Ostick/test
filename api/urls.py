from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url('article', views.showArticle, name="article"),
    url('reviews', views.showComment, name="review"),
    path('review/<int:pk>/', views.AddUpvotes.as_view(), name='add_upvotes'),
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
