###文章接口
* [根据文章ID删除指定文章](#post-destory)     
* [根据文章ID获取文章的内容](#post-show)
* [发布文章](#post-update)   
* [获取用户发布的文章](#posts-user)
* [上传图片并发布文章](#post/upload)

###评论接口
* [根据文章ID返回文章的评论列表](#comments-show) 
* [我发出的评论列表](#)
* [我收到的评论列表](#)
* [获取用户发送及收到的评论列表](#)
* [评论一条文章](#)
* [删除一条评论](#)
* [批量删除评论](#)
* [回复一条评论](#)   

###用户接口
* [获取用户信息](#)
* [获取用户的粉丝数、关注数、文章数](#)    
    
###关系
* [获取用户的关注列表](#)
* [获取共同关注的人列表](#)
* [获取双向关注的人列表](#)
* [获取用户的粉丝列表](#)
* [关注某用户](#)
* [取消关注某用户](#)

<h3 id='post-destory'>post/detory</h3>
---
根据文章ID删除指定文章
###URL
---
<http://127.0.0.1:8000/api/v1.0/post/destory>	
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
  "post_text": "去年冬天朋友赶会头卖水果，顾客：称点苹果。朋友：3块X8斤＝23块。你的3块X7斤正好20元。很快传开·····有个傻子在卖水果。结果一个下午不到满满的三轮车水果被抢购一空。收摊时卖祙子的大娘提醒：小伙子算不好账，下次一定得带上计算器。朋友：大娘你真当我傻呀，看看别的水果摊，他们倒是会算帐一下午又卖出去几斤？？",
  "post_id": "117668998",
  "comment_count": 22,
  "like_count": 944,
  "user": {
    "user_id": "31495449",
    "friends_count": 0,
    "gender": "m",
    "follers_count": 0,
    "article_count": 0,
    "avatar": "http://pic.qiushibaike.com/system/avtnew/3149/31495449/medium/20160404144203.jpg",
    "user_name": "憨豆先生不太逗"
  },
  "created_time": "2016-10-03 00:00:00+00:00"
}
```
<h3 id='post-show'>post/show</h3>
---
根据文章ID获取文章的内容
###URL
---
<http://127.0.0.1:8000/api/v1.0/post/show>	
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
查询的微博必须是授权用户发出的，非授权用户发出的将不返回数据；
###返回结果
---
**JSON示例**  

```
{
  "post_text": "去年冬天朋友赶会头卖水果，顾客：称点苹果。朋友：3块X8斤＝23块。你的3块X7斤正好20元。很快传开·····有个傻子在卖水果。结果一个下午不到满满的三轮车水果被抢购一空。收摊时卖祙子的大娘提醒：小伙子算不好账，下次一定得带上计算器。朋友：大娘你真当我傻呀，看看别的水果摊，他们倒是会算帐一下午又卖出去几斤？？",
  "post_id": "117668998",
  "comment_count": 22,
  "like_count": 944,
  "user": {
    "user_id": "31495449",
    "friends_count": 0,
    "gender": "m",
    "follers_count": 0,
    "article_count": 0,
    "avatar": "http://pic.qiushibaike.com/system/avtnew/3149/31495449/medium/20160404144203.jpg",
    "user_name": "憨豆先生不太逗"
  },
  "created_time": "2016-10-03 00:00:00+00:00"
}
```


<h3 id='comments-show'>comments/show</h3>
---
根据文章ID返回文章的评论列表
###URL
---
<http://127.0.0.1:8000/api/v1.0/comments/show.json>
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
post_id | true | int64 |需要查询文章的ID
since_id | false | int64 | 若指定此参数，则返回ID比since_id大的评论（即比since_id时间晚的评论）,默认为0
max_id | false | int64 | 若指定此参数，则返回ID小于或等于max_id的评论，默认为0
count | false | int | 单叶返回的纪录条数，默认为50
page | false | int | 返回结果的页码
filter_by_author | false | int | 作者筛选类型，0:全部、1:我关注的人 、2:陌生人 ，默认为0
###返回结果
---
***JSON示例***   

```   
{
  ghdsigh
}
```    
<h3 id="post-show">post/show</h3>
---
***根据文章ID获取文章的内容***
###URL
---
<http://127.0.0.1:8000/post/show>
###支持格式
---
***JSON***
###HTTP请求方式
---
***GET***
###是否需要登录
---
***是***

<h3 id='post-update'>post/update</h3>
---
发布文章
###URL
---
<http://127.0.0.1:8000/post/update>


