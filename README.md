# crawler_python
> 主要是一些python爬虫的代码
> 对于python爬虫爬取信息，主要是分两步
- 不需要登录的，直接打开网站目录，查找各个具体界面的网址，用正则表达式或是专门的工具匹配到网址，然后再对具体的网址进行分析，用同样的方式把信息爬取下来。
- 需要登录的，简单的可直接分析网页的表单，提交数据获取cookie，对于登录界面用js加载的，可抓包获取登录的网址，或直接用selenium模拟点击登录。
