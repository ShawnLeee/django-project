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
