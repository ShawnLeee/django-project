# encoding: utf-8
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from django.http import Http404
from models import QBPost, QBComment
from serializers import QBPostSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from uuid import uuid4
from django.contrib.auth.decorators import login_required
#from django.db import transaction


@login_required
def secret_page(request):
    return Response('Secret contents!', status=status.HTTP_200_OK)


class QBPostList(APIView):
    """
    List Post in page
    """
    def get(self, request, format=None):
        post_list = QBPost.objects.all()
        paginator = Paginator(post_list, 10)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        serializer = QBPostSerializer(posts, many=True)
        return Response(serializer.data)


class AddPost(APIView):

    def post(self, request):
        post_data = request.data
        post_id = uuid4().hex
        post_data['post_id'] = post_id
        serializer = QBPostSerializer(data=post_data)
        print(repr(serializer))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeletePost(APIView):

    def post(self, request):
        request_data = request.data
        post_id = request_data.get('post_id')
#       删除文章及文章的评论
        post = QBPost.objects.get(post_id=post_id)
        post_dict = post.to_dict()
        comments = QBComment.objects.filter(post_id=post_id)
        comments.delete()
        post.delete()
        return Response(post_dict, status.HTTP_200_OK)


class PostShow(APIView):
    def get(self, request):
        post_id = request.GET.get('post_id')
        post = QBPost.objects.get(post_id=post_id)
        return Response(post.to_dict(), status.HTTP_200_OK)


class CommentsShow(APIView):
    def get(self, request):
        post_id = request.GET.get('post_id')
        since_id = request.GET.get('since_id')
        max_id = request.GET.get('max_id')

        count = request.GET.get('count')
        if count is None:
            count = 50
        page = request.GET.get('page')
        if page is None:
            page = 1

        filter_by_author = request.GET.get('filter_by_author')
        if filter_by_author is None:
            filter_by_author = 0

        comments = QBComment.objects.filter(post_id=post_id).order_by('comment_id')

        if since_id is not None:
            comments = comments.filter(comment_id__gte=since_id)
        if max_id is not None:
            comments = comments.filter(comment_id__lte=max_id)

        paginator = Paginator(comments, count)

        try:
            comments = paginator.page(page)
        except PageNotAnInteger:
            comments = paginator.page(1)
        except EmptyPage:
            comments = paginator.page(paginator.num_pages)

        comments_array = [comment.to_dict() for comment in comments]
        res_dict = {'comments': comments_array}

        return Response(res_dict, status.HTTP_200_OK)


class PostsUser(APIView):
    def get(self, request):
        access_token = request.GET.get('access_token')
        uid = request.GET.get('uid')
        since_id = request.GET.get('since_id')
        max_id = request.GET.get('max_id')
        count = request.GET.get('count')
        page = request.GET.get('page')

        if page is None:
            page = 1
        if count is None:
            count = 20
        if count > 100:
            count = 100
        posts = QBPost.objects.filter(user=uid)

        if since_id is not None:
            posts = posts.filter(post_id__gte=since_id)
        if max_id is not None:
            posts = posts.filter(post_id__lte=max_id)

        paginator = Paginator(posts, count)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        posts_dict = {'posts': [post.to_dict() for post in posts]}
        return Response(posts_dict, status.HTTP_200_OK)


