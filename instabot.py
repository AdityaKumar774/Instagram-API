from API_access_token import ACCESS_TOKEN

import requests
from urllib import urlretrieve

# import matplotlib

BASE_URL = "https://api.instagram.com/v1/"


# function for getting self details
def getSelfDetails():
    url = BASE_URL + 'users/self/?access_token=' + ACCESS_TOKEN
    my_info = requests.get(url)
    my_info = my_info.json()
    if my_info['meta']['code'] == 200:
        print 'My user name is: ' + my_info['data']['username']
        print 'My user id is: ' + my_info['data']['id']
        print 'My name is: ' + my_info['data']['full_name']
        print 'I have ' + str(my_info['data']['counts']['media']) + ' posts'
        print str(my_info['data']['counts']['followed_by']) + ' people follow me on Instagram'
        print 'I follow ' + str(my_info['data']['counts']['follows']) + ' people on Instagram'
    else:
        print 'Code other than 200 received'


getSelfDetails()


# function to get my public posts
def myPublicPosts():
    url = BASE_URL + 'users/self/media/recent/?access_token=' + ACCESS_TOKEN
    my_post = requests.get(url)
    my_post = my_post.json()
    if my_post['meta']['code'] == 200:
        # print my_post
        # print 'My recent post\'s url is: ' + my_post['data'][0]['images']['standard_resolution']['url']
        print 'My recent post\'s id is: ' + my_post['data'][0]['id']
        urlretrieve(my_post['data'][0]['images']['standard_resolution']['url'], 'my_recent_post.jpg')
        print 'My recent post has been downloaded by the name my_recent_post.jpg'

    def recentLikedPost():
        media_url = BASE_URL + 'users/self/media/liked?access_token=' + ACCESS_TOKEN
        liked_post = requests.get(media_url)
        liked_post = liked_post.json()
        if liked_post['meta']['code'] == 200:
            print 'Recent liked post\'s id is: ' + liked_post['data'][0]['id']
            print 'This post belongs to: ' + liked_post['data'][0]['user']['full_name']
        else:
            print 'No response received from server side'

    recentLikedPost()


myPublicPosts()


# function to get other user's user id
def getUserId(userName):
    url = BASE_URL + 'users/search?q=' + userName + '&access_token=' + ACCESS_TOKEN
    info = requests.get(url)
    info = info.json()
    if info['meta']['code'] == 200:
        if len(info['data']):
            return info['data'][0]['id']
        else:
            print 'User does not exist'
            return 'none'
    else:
        print 'Status code other than 200 received\n'
        return 'none'


def getUserDetail():
    userName = raw_input('\nEnter User name which you want to search: \n')
    userId = getUserId(userName)
    url = BASE_URL + 'users/' + str(userId) + '/?access_token=' + ACCESS_TOKEN
    info = requests.get(url)
    info = info.json()
    print 'User\'s name is: ' + info['data']['full_name']
    print 'User\'s user id is: ' + info['data']['id']
    getUserPost(userId)


# function to get other user recent post id
def getUserPost(userId):
    url = BASE_URL + 'users/' + str(userId) + '/media/recent/?access_token=' + ACCESS_TOKEN
    info = requests.get(url)
    info = info.json()
    if info['meta']['code'] == 200:
        postId = info['data'][0]['id']
        print 'Recent post\'s id is: ' + str(postId)
        getUserPostContent(postId)
        likeUserPost(postId)
        commentUserPost(postId)
    else:
        print 'Code other than 200 received'


# function to get user's recent post content
def getUserPostContent(postId):
    url = BASE_URL + 'media/' + str(postId) + '?access_token=' + ACCESS_TOKEN
    info = requests.get(url)
    info = info.json()
    if info['meta']['code'] == 200:
        if info['data']['type'] == 'image':
            mediaUrl = info['data']['images']['standard_resolution']['url']
            urlretrieve(mediaUrl, 'image.jpg')
            print 'The recent post has been downloaded by the name image.jpg'
        elif info['data']['type'] == 'video':
            mediaUrl = info['data']['videos']['standard_resolution']['url']
            urlretrieve(mediaUrl, 'a.mp4')
            print 'The video has been downloaded by the name a.mp4'
    else:
        print 'Code other than 200 received'


# function to like user's recent post
def likeUserPost(postId):
    data = {
        'access_token': ACCESS_TOKEN
    }
    url = BASE_URL + 'media/' + str(postId) + '/likes'
    info = requests.post(url, data)
    info = info.json()
    if info['meta']['code'] == 200:
        print 'Post Liked!'
    else:
        print 'Code other than 200 received'

    # function to get media post by the popular hash tags
    def popularTags():
        tag_name = raw_input('\nEnter the popular tag you want to search for:\n')
        url = BASE_URL + 'tags/' + tag_name + '?access_token=' + ACCESS_TOKEN
        info = requests.get(url)
        info = info.json()
        if info['meta']['code'] == 200:
            info['data']['name'] == '#' + tag_name
            print 'Total number of tags by this name is: ' + str(info['data']['media_count'])
        else:
            print 'Code other than 200 received'

    # calling of function
    popularTags()


# function to comment on the post
def commentUserPost(postId):
    comment_text = raw_input('\nEnter the text which you want to comment to the user\'s post\n')
    data = {
        'access_token': ACCESS_TOKEN,
        'text': comment_text
    }
    url = BASE_URL + 'media/' + str(postId) + '/comments'
    info = requests.post(url, data)
    info = info.json()
    if info['meta']['code'] == 200:
        print 'Comment on post is: ' + str(data['text'])
        get_comment = BASE_URL + 'media/' + str(postId) + '/comments?access_token' + ACCESS_TOKEN
        comment_info = requests.get(get_comment)
        comment_info = comment_info.json()
        if comment_info['meta']['code'] == 200:
            comments = comment_info['data']
            print comments
    else:
        print 'Code other than 200 received'


# calling of the main function
getUserDetail()
