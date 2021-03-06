###文章接口
* [根据文章ID删除指定文章](#post-destory)     
* [根据文章ID获取文章的内容](#post-show)
* [发布文章](#post-update)   
* [获取用户发布的文章](#posts-user)
* [上传图片并发布文章](#post/upload)

###评论接口
* [根据文章ID返回文章的评论列表](#comments-show) 
* [我发出的评论列表](#comments-by_me)
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
<http://52.43.221.136/api/v1.0/post/destory>	
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
<http://52.43.221.136/api/v1.0/post/show>	
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
<http://52.43.221.136/api/v1.0/comments/show.json>
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
  "comments": [
    {
      "comment_text": "图呢？",
      "floor": 6,
      "comment_id": "366140615",
      "user": {
        "user_id": "31960253",
        "friends_count": 0,
        "gender": "m",
        "follers_count": 0,
        "article_count": 0,
        "avatar": "http://pic.qiushibaike.com/system/avtnew/3196/31960253/medium/2016091221264454.JPEG",
        "user_name": "廻憶"
      },
      "created_time": "2016-10-04 10:50:03.693990+00:00",
      "post": {
        "post_text": "：喂，哥们你在家忙啥呢？：这不是你出差一个月了，你家责任田太旱了，嫂子让我帮忙浇地呢。：你这禽兽，你·····你·····：我真的在帮忙浇地！！",
        "post_id": "117665680",
        "comment_count": 25,
        "like_count": 3476,
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
    },
    {
      "comment_text": "你家有地",
      "floor": 7,
      "comment_id": "366141087",
      "user": {
        "user_id": "12402200",
        "friends_count": 0,
        "gender": "m",
        "follers_count": 0,
        "article_count": 0,
        "avatar": "http://pic.qiushibaike.com/system/avtnew/1240/12402200/medium/20140807223634.jpg",
        "user_name": "赣南第一鞭"
      },
      "created_time": "2016-10-04 10:50:03.693990+00:00",
      "post": {
        "post_text": "：喂，哥们你在家忙啥呢？：这不是你出差一个月了，你家责任田太旱了，嫂子让我帮忙浇地呢。：你这禽兽，你·····你·····：我真的在帮忙浇地！！",
        "post_id": "117665680",
        "comment_count": 25,
        "like_count": 3476,
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
    }
  ]
}
```    
<h3 id='comments-by_me'>comments/by_me.json</h3>
---
获取用户所发出的评论列表
###URL
---
<http://52.43.221.136/api/v1.0/comments/by_me.json>
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
user_id | true | int64 |需要查询的作者ID
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
  "comments": [
    {
      "comment_text": "图呢？",
      "floor": 6,
      "comment_id": "366140615",
      "user": {
        "user_id": "31960253",
        "friends_count": 0,
        "gender": "m",
        "follers_count": 0,
        "article_count": 0,
        "avatar": "http://pic.qiushibaike.com/system/avtnew/3196/31960253/medium/2016091221264454.JPEG",
        "user_name": "廻憶"
      },
      "created_time": "2016-10-04 10:50:03.693990+00:00",
      "post": {
        "post_text": "：喂，哥们你在家忙啥呢？：这不是你出差一个月了，你家责任田太旱了，嫂子让我帮忙浇地呢。：你这禽兽，你·····你·····：我真的在帮忙浇地！！",
        "post_id": "117665680",
        "comment_count": 25,
        "like_count": 3476,
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
    },
    {
      "comment_text": "你家有地",
      "floor": 7,
      "comment_id": "366141087",
      "user": {
        "user_id": "12402200",
        "friends_count": 0,
        "gender": "m",
        "follers_count": 0,
        "article_count": 0,
        "avatar": "http://pic.qiushibaike.com/system/avtnew/1240/12402200/medium/20140807223634.jpg",
        "user_name": "赣南第一鞭"
      },
      "created_time": "2016-10-04 10:50:03.693990+00:00",
      "post": {
        "post_text": "：喂，哥们你在家忙啥呢？：这不是你出差一个月了，你家责任田太旱了，嫂子让我帮忙浇地呢。：你这禽兽，你·····你·····：我真的在帮忙浇地！！",
        "post_id": "117665680",
        "comment_count": 25,
        "like_count": 3476,
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
    }
  ]
}
```    
<h3 id="post-show">post/show</h3>
---
***根据文章ID获取文章的内容***
###URL
---
<http://52.43.221.136/post/show>
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
<http://52.43.221.136/post/update>

<h3 id='posts-user'>posts/user</h3>
---
获取用户发布的文章
###URL
---
<http://52.43.221.136/api/v1.0/posts/user>	
###支持格式
---
***JSON***
###HTTP请求方式
---
***GET***
###是否需要登录
---
***是***
###请求参数
---
参数 | 必选 | 类型及范围 | 说明 
--- | ---- | -------- | ---
access_token | true | string | 采用Oauth授权方式为必填参数,OAuth授权后获得
uid | true | int64 | 需要查询的用户ID
since_id | false | int64 | 若指定此参数，则返回ID比since_id大的文章（即比since_id时间晚的文章），默认为0。
max_id | false | int64 | 若指定此参数，则返回ID小于或等于max_id的文章，默认为0。
count | false | int | 单页返回的记录条数，最大不超过100，超过100以100处理，默认为20。
page | false | int | 返回结果的页码，默认为1。
###注意事项
---
###返回结果
---
**JSON示例**  

```
{
  "posts": [
    {
      "post_text": "节日？我们认识吗？小店单身汉那有时间和空间去过什么节日，没钱什么都不是！大家都挺忙的，真的！等你有钱了，天天都是节日！",
      "post_id": "113134415",
      "comment_count": 2,
      "like_count": 133,
      "user": {
        "user_id": "19629703",
        "friends_count": 0,
        "gender": "m",
        "follers_count": 0,
        "article_count": 0,
        "avatar": "http://pic.qiushibaike.com/system/avtnew/1962/19629703/medium/20150625122541.jpg",
        "user_name": "欠炮轰的星"
      },
      "created_time": "2015-10-01 00:00:00+00:00"
    },
    {
      "post_text": "有麻烦又有多少人报警求助所谓的正义使者，我相信那里头有真正的正义使者，但我从未想过要和他们接触。因为假正义使者太多太多，除非我真遇到大事了！和我一样点一个呗……",
      "post_id": "115844283",
      "comment_count": 7,
      "like_count": 304,
      "user": {
        "user_id": "19629703",
        "friends_count": 0,
        "gender": "m",
        "follers_count": 0,
        "article_count": 0,
        "avatar": "http://pic.qiushibaike.com/system/avtnew/1962/19629703/medium/20150625122541.jpg",
        "user_name": "欠炮轰的星"
      },
      "created_time": "2016-04-05 00:00:00+00:00"
    }
  ]
}
```



