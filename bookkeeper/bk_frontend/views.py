from bookkeeper.settings import HOST, CLIENT_ID
from django.shortcuts import render
import requests
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    if request.method == 'GET':
        data = request.DATA
        username = data.get('username')
        password = data.get('password')
        client_id = CLIENT_ID
        host = HOST
        r = requests.post(host + '/o/token/', data={'client_id': client_id,
                                                    'grant_type': 'password',
                                                    'username': username,
                                                    'password': password})
        r_data = r.json()
        token = r_data.get('access_token')
        token_type = r_data.get('token_type')
        user = User.objects.get(username=username)
        response = requests.get(host + '/api/user' + str(user.id) + '/',
                                headers={
                                    'Authorization': token_type + ' ' + token})
        from ipdb import set_trace; set_trace()

