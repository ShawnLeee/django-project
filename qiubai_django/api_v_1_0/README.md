[1.post/destory](#post-destory)   
[2.comments/show](#comments-show)   


<h3 id='post-destory'>post/detory</h3>
---
根据文章ID删除指定文章
###URL
---
<http://127.0.0.1:8000/post/destory>	
###支持格式
---
***JSON***
###HTTP请求方式
---
***POST***
###是否需要登录
---
***是***
###请求参数
---
参数 | 必选 | 类型及范围 | 说明 
--- | ---- | -------- | ---
access_token | true | string | 采用Oauth授权方式为必填参数,OAuth授权后获得
post_id | true | int64 | 需要删除的文章的id
###注意事项
---
只能删除自己发布的文章
###返回结果
---
**JSON示例**  

```
{
    "created_at": "Tue May 31 17:46:55 +0800 2011",
    "id": 11488058246,
    "text": "求关注。"，
    "source": "<a href="http://weibo.com" rel="nofollow">新浪微博</a>",
    "favorited": false,
    "truncated": false,
    "in_reply_to_status_id": "",
    "in_reply_to_user_id": "",
    "in_reply_to_screen_name": "",
    "geo": null,
    "mid": "5612814510546515491",
    "reposts_count": 8,
    "comments_count": 9,
    "annotations": [],
    "user": {
        "id": 1404376560,
        "screen_name": "zaku",
        "name": "zaku",
        "province": "11",
        "city": "5",
        "location": "北京 朝阳区",
        "description": "人生五十年，乃如梦如幻；有生斯有死，壮士复何憾。",
        "url": "http://blog.sina.com.cn/zaku",
        "profile_image_url": "http://tp1.sinaimg.cn/1404376560/50/0/1",
        "domain": "zaku",
        "gender": "m",
        "followers_count": 1204,
        "friends_count": 447,
        "statuses_count": 2908,
        "favourites_count": 0,
        "created_at": "Fri Aug 28 00:00:00 +0800 2009",
        "following": false,
        "allow_all_act_msg": false,
        "remark": "",
        "geo_enabled": true,
        "verified": false,
        "allow_all_comment": true,
        "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
        "verified_reason": "",
        "follow_me": false,
        "online_status": 0,
        "bi_followers_count": 215
    }
}
```

<h3 id='comments-show'>comments/show</h3>
---
根据微博ID返回某条微博的评论列表
###URL
---
<http://127.0.0.1:8000/comments/show.json>
###支持格式
---
**JSON**
###HTTP请求方式
---
***GET***
###是否需要登录
---
**是**
###请求参数
参数 | 必选 | 类型及范围 | 说明  
--- | --- | --- | --- 
access_token | true | string | 采用OAuth授权方式为必填参数,OAuth授权后获得 
