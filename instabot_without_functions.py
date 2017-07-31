import requests
import urllib

self_url = 'https://api.instagram.com/v1/users/self/?access_token=1545666056.98346f2.38c9a48c189d43dd88ffe4b45bbd9d38'
self_details = requests.get(self_url)
self_details = (self_details.json())
# print self_details
if self_details['meta']['code'] == 200:
    my_user_id = self_details['data']['id']
    print ('My user id is: ' + my_user_id)
    my_full_name = self_details['data']['full_name']
    print ('My full name is: ' + my_full_name)
    my_profile_pic = self_details['data']['profile_picture']
    print ('Url of my profile picture is: ' + my_profile_pic)
    my_bio = self_details['data']['bio']
    print ('My bio is: ' + my_bio)
    my_website = self_details['data']['website']
    print ('My website is: ' + my_website)
    my_posts = self_details['data']['counts']['media']
    print ('I have ' + str(my_posts) + ' posts')
    my_followers = self_details['data']['counts']['followed_by']
    print (str(my_followers) + ' people follow me on Instagram')
    i_follow = self_details['data']['counts']['follows']
    print ('I follow ' + str(i_follow) + ' people on Instagram\n')
else:
    print 'Something went wrong, contact administrator for support'

my_url = 'https://api.instagram.com/v1/users/' + my_user_id + '/media/recent/?access_token=1545666056.98346f2.38c9a48c189d43dd88ffe4b45bbd9d38'
my_details = requests.get(my_url)
my_details = (my_details.json())
# print my_details
if my_details['meta']['code'] == 200:
    my_recent_post_id = my_details['data'][0]['id']
    print ('My recent post\'s id is: ' + str(my_recent_post_id))
    my_recent_post_url = my_details['data'][0]['images']['standard_resolution']['url']
    print ('Url of my recent post is: ' + my_recent_post_url)
    urllib.urlretrieve(my_recent_post_url, 'recent_post_pic.jpg')
    print 'The image has been downloaded with name recent_post_pic.jpg'
else:
    print 'Something went terribly wrong, contact administrator for support'

other_user_name = raw_input('\nEnter the username which you want to search: \n')
user_url = 'https://api.instagram.com/v1/users/search?q=' + other_user_name + '&access_token=1545666056.98346f2.38c9a48c189d43dd88ffe4b45bbd9d38'
other_user_details = requests.get(user_url)
other_user_details = (other_user_details.json())
# print other_user_details
if other_user_details['meta']['code'] == 200:
    other_user_user_id = other_user_details['data'][0]['id']
    print ('User\'s user id is: ' + str(other_user_user_id))
else:
    print 'User does not exist'

other_user_post_url = 'https://api.instagram.com/v1/users/' + other_user_user_id + '/media/recent/?access_token=1545666056.98346f2.38c9a48c189d43dd88ffe4b45bbd9d38'
other_user_posts = requests.get(other_user_post_url)
other_user_posts = (other_user_posts.json())
# print other_user_posts
if other_user_posts['meta']['code'] == 200:
    other_user_post_id = other_user_posts['data'][0]['id']
    print ('Id of recent post is: ' + other_user_post_id)
    other_user_recent_post_url = other_user_posts['data'][0]['images']['standard_resolution']['url']
    print ('Url of most recent post of user is: ' + other_user_recent_post_url)
    urllib.urlretrieve(other_user_recent_post_url, 'other_user_recent_post.jpg')
    print ('The most recent post of user with user id has been downloaded by name other_user_recent_post.jpg')
    likes_on_post = other_user_posts['data'][0]['likes']['count']
    print ('Likes on this post is: ' + str(likes_on_post))
    requests.post(
        'https://api.instagram.com/v1/media/' + other_user_post_id + '/likes?access_token=1545666056.98346f2.38c9a48c189d43dd88ffe4b45bbd9d38'.format(
            other_user_post_id), other_user_details)
    print 'You Liked this post!'
    comment_text = {'access_token': '1545666056.98346f2.38c9a48c189d43dd88ffe4b45bbd9d38',
                    'text': 'Awesome'
                    }
    requests.post('https://api.instagram.com/v1/media/' + other_user_post_id + '/comments', comment_text)
    print 'You Commented on this post'

    comments_on_post = other_user_posts['data'][0]['comments']['count']
    print ('User has ' + str(comments_on_post) + ' comments on this post')