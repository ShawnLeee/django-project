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
        post = QBPost.objects.filter(post_id=post_id)
        comments = QBComment.objects.filter(post_id=post_id)
        try:
            post.delete()
            comments.delete()
        except:
            return Response('failed', status.HTTP_400_BAD_REQUEST)
        print post_id
        print comments
        return Response('', status.HTTP_200_OK)

