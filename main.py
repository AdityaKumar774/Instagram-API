import requests
import urllib

url = 'https://api.instagram.com/v1/users/1472346217/media/recent/?access_token=1545666056.98346f2.38c9a48c189d43dd88ffe4b45bbd9d38'
user_details = requests.get(url)
user_details = (user_details.json())
# print (user_details)
if user_details['meta']['code'] == 200:
    user_name = user_details['data'][0]['user']['full_name']
    print('User Name is: ' + user_name)
    user_id = user_details['data'][0]['user']['id']
    print('User Id is: ' + user_id)
    media_id = user_details['data'][0]['id']
    print ('Recent Post\'s id: ' + media_id)
    image_url = user_details['data'][0]['images']['standard_resolution']['url']
    print ('Url of first post: ' + image_url)
    likes = user_details['data'][0]['likes']['count']
    print ('This image has: ' + str(likes) + ' likes')
    comments = user_details['data'][0]['comments']['count']
    print ('This image has: ' + str(comments) + ' comments')
    urllib.urlretrieve(image_url)
else:
    print ('No User Found')