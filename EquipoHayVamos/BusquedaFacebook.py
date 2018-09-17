import facebook

TOKEN = "" # Your GraphAPI token here.

graph = facebook.GraphAPI(access_token=TOKEN, version="2.7")
posts = graph.search(q="aquafresh", type="post")

print posts['data']
