import requests

url = 'https://api.instagram.com/v1/users/search?q=abhishek_parmar.insta&access_token=1545666056.98346f2.38c9a48c189d43dd88ffe4b45bbd9d38'
user_details = requests.get(url)
print(user_details.json())
