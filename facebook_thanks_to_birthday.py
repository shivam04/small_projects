import facebook
import datetime

access_token = 'Enter Access Token'
user = 'me'
birthday = 'YYYY-mm-dd'  
def parse_date(post):
    post_date = datetime.datetime.strptime(
        post['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
    return post_date.date()
 
 
def comment(post):
    message = "Thank You! :)"
    graph.put_comment(post['id'], message)
 

bday = datetime.datetime.strptime(birthday, '%Y-%m-%d')
print bday.date() 

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'feed')

birthday_posts = [
    post for post in posts['data'] if parse_date(post) == bday.date()]

for n, post in enumerate(birthday_posts):
    comment(post)
    print('Post successfully')
