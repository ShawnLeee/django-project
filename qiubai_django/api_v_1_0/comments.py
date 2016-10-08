# encoding: utf-8
from django.http import HttpRequest
from models import QBComment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_comments(request):
    '''
    :type request:HttpRequest
    '''
    post_id = request.GET.get('post_id')

    user_id = request.GET.get('user_id')
    print user_id

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
    comments = None
    if post_id is not None:
        comments = QBComment.objects.filter(post_id=post_id).order_by('comment_id')
    elif user_id is not None:
        comments = QBComment.objects.filter(user_id=user_id).order_by('comment_id')
    else:
    	return {'comments': []}

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

    return res_dict



