import requests
import json
import webbrowser

project_id='<insert tracker project id here as string>'
tracker_token='<insert tracker token here as string>'

url = 'https://www.pivotaltracker.com/services/v5/projects/' + project_id + '/memberships'

response = requests.get(url, headers={'X-TrackerToken': tracker_token})

if(response.ok):
    jData = json.loads(response.content)
    mail_list = []
    for x in jData:
        # print x['person']['email']
        mail_list.append(x['person']['email'])
    for x in mail_list: print x
    email_to = ";".join(mail_list)
    # print "mailto:" + str(email_to)
    webbrowser.open("mailto:" + str(email_to))

else:
    print ("OOPS!, REST response bad :{}")
