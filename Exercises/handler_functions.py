import boto3


def handler(event, context):
    body = event['body']
    client = boto3.client('secretsmanager')
    secret = body['secretId']
    url = body['url']
    action = body['action']
    return client, secret, url, action 

def makeAPICall(client, secret, url, action):
    ''' 
        Based on each action perform a different api call for POST update the secret value 
        using the URL and for GET retrieve the secret value instead
    '''
    if 'GET' in action:
        print('The action is GET')
    elif 'POST' in action:
        print('The action is POST')
    else:
        print('The action must be either "GET" or "POST"')

def main():
# action should be "GET" or "POST"
    event = { "body" : { "secretId": "myTestSecret", "url": "google.com", "action": "GET"}}
    context = "placeholder"
    makeAPICall(*handler(event, context))

if __name__ == '__main__':
    main()
