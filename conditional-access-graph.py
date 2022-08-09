# Copyright (C) 2022  Agustinus Marcello S

# !/usr/bin/python3
# -*- coding: utf-8 -*-

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/

import requests
import json

ca_url = 'https://graph.microsoft.com/v1.0/identity/conditionalAccess/policies' # url conditional access graph
app_id="<APPLICATION ID>" # app id dapat dilihat dari -> Azure AD -> App registrations -> Application ID
client_secret="<CLIENT SECRET>" # client secret didapatkan dari -> Azure AD -> Client secrets -> New client secret -> copy the Value
token_url = 'https://login.microsoftonline.com/<TENANT ID>/oauth2/token' # Tenant ID dapat dilihat dari halaman Overview Azure Active Directory

bodydata = {
    "displayName": "Block Access O365 pada Jam Tertentu saja", # penamaan policy Conditional Access
    "state": "enabled",
    "conditions": {
        "applications": {
            "includeApplications": [
                "cc15fd57-2c6c-4117-a88c-83b1d56b4bbe",'Office365' # dapat diubah sesuai kebutuhan
            ]
        },
        "users": {
         "includeUsers": ['All'], # dapat diubah sesuai kebutuhan
        }
    },
    "grantControls": {
        "operator": "OR",
        "builtInControls": [
            "block"
        ]
    }
}

token_data = {
 'grant_type': 'password',
 'client_id': app_id,
 'client_secret': client_secret,
 'resource': 'https://graph.microsoft.com',
 'scope':'https://graph.microsoft.com',
 'username':'<EMAIL/ACCOUNT ADMINISTRATOR>', # Account with no 2MFA
 'password':'<PASSWORD>', # Password
}

token_r = requests.post(token_url, data=token_data)
token = token_r.json().get('access_token')

headers = {
 'Authorization': 'Bearer {}'.format(token)
}

getlist_ca=json.loads(requests.get(ca_url,headers=headers).text)

list_ca=list(getlist_ca["value"])

def search(values, searchFor): # fungsi untuk mencari apakah policy sudah ada atau belum berdasarkan penamaan policy
    global id_existing
    for i in values:
        if searchFor in i['displayName']:
            id_existing=i['id']
            return i['displayName']
    return None

if search(list_ca,bodydata["displayName"]): # kondisi ketika policy SUDAH ADA berdasarkan penamaan policy maka dilakukan delete request
    print('policy Conditional Access yang akan dihapus -> ID = '+id_existing)
    test_delete_ca = requests.delete(ca_url+'/'+id_existing, headers=headers, json=bodydata)
    print('policy tersebut sudah berhasil dihapus')

else: # kondisi ketika policy BELUM ADA berdasarkan penamaan policy maka dilakukan post request
    test_post_ca = json.loads(requests.post(ca_url, headers=headers, json=bodydata).text)
    print('policy Conditional Access belum ada dan akan dibuat')
    print('berhasil')

