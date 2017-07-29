import requests

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
else:
    print ('No User Found')