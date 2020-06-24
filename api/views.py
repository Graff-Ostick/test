from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ArticleSerializer, ReviewSeriallizer
from .models import Article, Review
import schedule


def addUpvote(request,pk):
    articles = Article.objects.get(id=pk)
    if request.method == "POST":
        articles.upvotes +=1
        articles.save()
    return showArticle(request)

def addComment(request,pk):
    article = Article.objects.get(id=pk)
    reviews = Review.objects.filter(article=pk)
    name = request.POST.get("name")
    text = request.POST.get("comment")
    if request.method == "POST":
        if name or text:
            reviews.create(name=name, text=text, article=article)
    return render(request, 'comment.html', {"reviews": reviews})

def showArticle(request):
    articles = Article.objects.all()
    return render(request, 'article.html', {"article":articles})

def showCurrentCommet(request,pk):
    reviews = Review.objects.filter(article=pk)
    return render(request, 'comment.html', {"reviews":reviews})

def showComment(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {"reviews":reviews})

@api_view(['GET'])
def apiView(request):
    api_urls = {
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
    }
    return Response(api_urls)

@api_view(['GET'])
def ArticleList(request):
    article = Article.objects.all()
    serializer = ArticleSerializer(article, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ArticleReview(request, pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializer(article, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def ArticleCreate(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    '''reset upvotes everyday '''
    schedule.every().day.at("00:00").do(Article.resetUpvotes())

    return Response(serializer.data)

@api_view(['POST'])
def ArticleUpdate(request, pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializer(instance=article, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def ArticleDelete(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return Response("Article deleted")

'''api review'''

@api_view(['GET'])
def CheckAllReview(request):
    review = Review.objects.all()
    serializer = ReviewSeriallizer(review, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def CheckArticleReview(request, pk, pk1):
    '''first search article - pk, than in them search id of comment'''
    review = Review.objects.filter(article=pk).filter(id=pk1)
    serializer = ReviewSeriallizer(review, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def AddReview(request):
    serializer = ReviewSeriallizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def UpdateReview(request, pk, pk1):
    review = Review.objects.filter(article=pk).filter(id=pk1)
    serializer = ArticleSerializer(instance=review, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteReview(request, pk, pk1):
    review = Review.objects.filter(article=pk).filter(id=pk1)
    review.delete()
    return Response("Review deleted")