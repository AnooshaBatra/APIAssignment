import requests,json

url = "https://app.flowdash.com/api/v1/workflows/bbI4Dl/tasks"

payload = ""
headers = {
  'Authorization': 'Bearer BBC5Hmx0zhSGPFCpTXVP6YyQ'
}

response = requests.request("GET", url, headers=headers, data=payload)




json_string = response.text

data = json.loads(json_string)

print(data)