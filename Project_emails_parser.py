import requests
import json

project_id='<insert tracker project id here as string>'
tracker_token='<insert tracker token here as string>'

url = 'https://www.pivotaltracker.com/services/v5/projects/' + project_id + '/memberships'

response = requests.get(url, headers={'X-TrackerToken': tracker_token})

if(response.ok):
    jData = json.loads(response.content)
    for x in jData:
        print x['person']['email']

else:
    print ("OOPS!, REST response bad :{}")
