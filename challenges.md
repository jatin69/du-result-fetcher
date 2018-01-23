# Challenges

- [X] Retriving sent POST values
- [X] Making it work for single course | single semester



##  VIEWSTATE ISSUE

Each request is accompanied by viewstate calculated based on values, options, controls and encoded to base64. 
Also there seems to be a 20 byte hash at the end of the content.

One probable solution is to 
[decode the viewstate](http://viewstatedecoder.azurewebsites.net/)
, change it as per new values, re inject it. But this is too much work. We can 
[attempt to hack](https://www.jardinesoftware.net/2012/09/17/viewstate-xss-whats-the-deal/) 
into viewstate with 
[Fiddler](https://www.telerik.com/fiddler) 
but chances are slim. Also, if the asp.net version gets updated on the server, there are chances that the decoding may consider
some more control values, essentially changing the viewstate. Though, this is a shallow problem and can be solved if we fetch 
new viewstate value from page programmatically, and inject our modification.

But, 
Viewstate is by default tamper proof if all features are enabled and
[can't be easily hacked](https://security.stackexchange.com/questions/18652/is-this-a-viewstate-attack)
, so spending time to crack it might not be a good idea.

#### An alternative approach

Crawl the site and find all possible combinations of form values programmatically, reach the final state of all, 
and derive viewstate of all and store as files. Then access as and when required.

[Scrapy](https://scrapy.org/) can help here. 
[see this example](https://blog.scrapinghub.com/2016/04/20/scrapy-tips-from-the-pros-april-2016-edition/).
It seems to fit our need. we will need to observe each viewstate, as it approaches options. Maybe we will also need to append form data at each stage to make it work correctly.

References - 
- [submit query to aspx in python](https://stackoverflow.com/questions/1480356/how-to-submit-query-to-aspx-page-in-python)
- [Programmatically Posting Data to ASP .NET Web Applications](http://dotnet.sys-con.com/node/45127)
- Go for [selenium](http://www.seleniumhq.org/) in python 2.x if needed. Maybe MechanicalSoup for python 3.x
