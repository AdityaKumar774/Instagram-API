import requests                                                                     # import libraries
import urllib

url = 'https://api.instagram.com/v1/users/1472346217/media/recent/?access_token=1545666056.98346f2.38c9a48c189d43dd88ffe4b45bbd9d38'
user_details = requests.get(url)                                                   # get request from the url
user_details = (user_details.json())                                               # convert it to json
# print (user_details)
if user_details['meta']['code'] == 200:
    user_name = user_details['data'][0]['user']['full_name']                        # get user name
    print('User Name is: ' + user_name)                                             # print user name
    user_id = user_details['data'][0]['user']['id']                                 # get user id
    print('User Id is: ' + user_id)                                                 # print user id
    media_id = user_details['data'][0]['id']                                        # get id of recent post
    print ('Recent Post\'s id: ' + media_id)                                        # print id of recent post
    image_url = user_details['data'][0]['images']['standard_resolution']['url']     # get image url
    print ('Url of first post: ' + image_url)                                       # print image url
    likes = user_details['data'][0]['likes']['count']                               # get likes on that image
    print ('This image has: ' + str(likes) + ' likes')                              # print number of likes
    comments = user_details['data'][0]['comments']['count']                         # get number of comments
    print ('This image has: ' + str(comments) + ' comments')                        # print number of comments
    urllib.urlretrieve(image_url, 'a.jpg')                                          # download the media
    print 'The image has been downloaded with name a.jpg'
else:
    print ('No User Found')