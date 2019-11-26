import json


def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        print("invalid json: %s" % error)
        return False
		
		

data = {
  "statusCode": 200,
  "headers": {
    "x-custom-header": "my custom header value"
  },
  "body": {
    "message": "Date is  1:53AM on Sep 02, 2019"
  }
}
json_data = json.dumps(data)
print(json_validator(json_data))

print (json_data)