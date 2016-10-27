# encoding: utf-8
# from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
# from django.http import Http404
from django.http import HttpRequest
from models import QBPost, QBComment, QBUser, QBPostPic
from serializers import QBPostSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from uuid import uuid4
from django.contrib.auth.decorators import login_required
from comments import get_comments
from PIL import ImageFile
# import ImageFile
#from django.db import transaction


class LoginView(APIView):
    def get(self, request):
        user = request.user
        print user
        return Response({'dshig':'sdhigod'}, status.HTTP_200_OK)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = QBUser.objects.get(user_name=username)
        token = Token.objects.create(user=user)
        print token.key
        return Response({'username':user.user_name, 'user_id':user.user_id}, status.HTTP_200_OK)


@login_required
def secret_page(request):
    return Response('Secret contents!', status=status.HTTP_200_OK)


class QBPostList(APIView):
    """
    List Post in page
    """
    def get(self, request):
        '''
        :type request:HttpRequest
        '''
        if request.user.is_authenticated:
            print(request.user)
        else:
            print(request.user)
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
        resdict = get_comments(request)
        return Response(resdict, status.HTTP_200_OK)

class UserComments(APIView):
    def get(self, request):
        resdict = get_comments(request)
        return Response(resdict, status.HTTP_200_OK)
        
        

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


class Upload(APIView):
    def post(self, request):
        user_id = request.POST.get('user_id')
        post_text = request.POST.get('post_text')

        post = QBPost.new_post_with(post_text=post_text, user_id=user_id)
        pics = []

        files = request.FILES.getlist('pic')
        for f in files:
            parser = ImageFile.Parser()
            for chunk in f.chunks():
                parser.feed(chunk)
            img = parser.close()
            imgpath = os.path.join(settings.MEDIA_URL, uuid4().hex+'.jpeg')
            img_abs_path = os.path.join(settings.BASE_DIR, imgpath)
            img.save(img_abs_path)
            post_pic = QBPostPic(pic_id=uuid4().hex, post_id=post.post_id, pic_url=imgpath)
            pics.append(post_pic)

        try:
            post.save()
            for pic in pics:
                pic.save()
        except:
            raise ValueError

        post_dict = post.to_dict()

        return Response(post_dict, status.HTTP_200_OK)

