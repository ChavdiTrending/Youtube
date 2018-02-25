import requests
import json
cnt = 0
nextpage = ''
links = []
while cnt<2:
	payload = {'part': 'id', 'key': 'AIzaSyA46dBqdBBtnfgxr8aRvSBE2Q7qiNyhWrk', 'maxResults': '50','chart':'mostPopular','regionCode':'IN','pageToken':nextpage}
	l = requests.Session().get('https://www.googleapis.com/youtube/v3/videos', params=payload)    
	resp_dict = json.loads(l.content)
	print(resp_dict)
	nextpage = resp_dict['nextPageToken']
	for i in resp_dict['items']:
	     links.append("https://youtu.be/"+i['id'])
	cnt+=1
jsonDict = {}
jsonDict['links'] = links
with open('Videolinks.json', 'w') as outfile:  
    json.dump(jsonDict, outfile)