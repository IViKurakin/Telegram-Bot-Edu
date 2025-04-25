'''
Client ID: 9c607f1c-46ef-49d4-8b3b-bc45a6bb13f4
Scope: GIGACHAT_API_PERS
Authorization Key: OWM2MDdmMWMtNDZlZi00OWQ0LThiM2ItYmM0NWE2YmIxM2Y0OjM4YjBkMjI1LTFkNTgtNGFkMC04MmQ3LWJkNTNkM2JkMjViNg==
Client Secret: 38b0d225-1d58-4ad0-82d7-bd53d3bd25b6
'''
# 1. Получение Access-token
import requests

url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
scope = 'GIGACHAT_API_PERS'
authKey = 'OWM2MDdmMWMtNDZlZi00OWQ0LThiM2ItYmM0NWE2YmIxM2Y0OjM4YjBkMjI1LTFkNTgtNGFkMC04MmQ3LWJkNTNkM2JkMjViNg=='
clientSecret = '38b0d225-1d58-4ad0-82d7-bd53d3bd25b6'
payload={
  'scope': scope
}
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
  'RqUID': clientSecret,
  'Authorization': f'Basic {authKey}'
}
response = requests.request("POST", url, headers=headers, data=payload, verify=False)
print(response.text)


# 2. Отправка запроса и получение ответа

import requests
url = "https://gigachat.devices.sberbank.ru/api/v1/models"
accessToken = 'eyJjdHkiOiJqd3QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiUlNBLU9BRVAtMjU2In0.FkXSvzaD82Lrz7dw-_Kgu3kVSEcAeBPlUBJOmkDdbIYqio9WBkAB_-0NU-eu3cTlWHUxM-dSE9Wu5SUlW1eEpRudmr5oKowHFIzmTNimzkygLhVBUMgHY75ddaFk1fYu41FCSJVteLcjYHC9_bj9w26cE6lSmMT_0d1bFbFHJ-wMLYIANpu2V58zJD6RK8UWQv82wKlTnLheoRPcOLgJ46_HnKbO22QO4eniGttJKRfijOJwixGnwRRKYJGVgi3VhVrWWM3tyxaV7p0fXeC7V843db-f-b0llYs0xB5UMmndDzzRveXWr4NbZdH9HeuOgYKHa4kjIjEbnxSUJlzocQ.u1paXyK_-4HcBk3j7cYW5Q.e0BkR3yAHafbE0ayfzjEXRmXRDVrB6TIY9QgJAGghWBGHStPUasBMGnMuOtTpecQNYg8jeUuuMQZk7SYek3l18-Fc2ECRNGP8TR93v2q1RQGcpyM91mor22_rRW0Z3VnMSqLc9gbUepNMIiwW4BTWNLgSFZ8a7V2xRTREDG1wbX2gORG0ktb01Mny51DOiXWT_Oe8xSOSrAPkhY67R6-9TbK-cUM02GtSf9e9_Uf6lPiYQA0lijUH9zwz5Z4uov7QQ0CWL7nOH9qJQS9_rhH4NWNSU5ZGSg8MGX0dAh6xu2UCZMjgIP4PNkwwy9sgK3f-Ast0efBcwss5FO8tNTbLpDpONQjqZPWUc73VO0PBKtQxpfOjutT3rnG7_PVqk_yX5wtY-ko7VKhZLyqoi5IvVHzbfpmyYvlgPMhpPEk0Pe7OdTsVBZ6KUbXZFM8NPfJOdi6YK4lN_EEJaGrsSNtVgNn1UnObSAGb_3CPilbTqp6o0yU94GDkETVLgAKbQt7EpaV2exnkpeCELFMRfl0hA8MO4zL-9NtQSWUiD84eaFb3XZz4SRgg9HsYVZ9sjYABxWRJGJhn266ShVr7ik7S3LEEwIu1VV0pfATBIPQnTtIy51X3cMvEdzf0KQQZEpWKkKQNsYXUtGPXT0duQ5iae2M8KerBqIM9ygwxYmj1LWuHsKu9u1LFsWYiuhybMVvSTlmig6qIqyfwl_WsXiJZCEvi90aZ-W2dNueuHw0pmM.3N0F4J5sTDLthdm3IoOxmaFNuM0EiaGLkqWzevJHE8s'
payload={}
headers = {
  'Accept': 'application/json',
  'Authorization': f'Bearer {accessToken}',
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)