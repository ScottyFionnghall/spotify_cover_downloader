import requests
import shutil
f = open('link.txt','r',encoding='utf-8')
playlsts = f.read()
playlsts = playlsts.split('\n')
playlsts = [line for line in playlsts if line.strip() != ""]
f.close()
for i in playlsts:
    spot_oembed = requests.get('https://open.spotify.com/oembed?url='+str(i))
    url = spot_oembed.json()['thumbnail_url']
    name = str(spot_oembed.json()['title']).replace(':',' ')
    response = requests.get(url, stream=True)
    with open(str(name).strip('?!;.,')+'.png', 'wb') as out_file:
        print('Getting cover from playlist "'+name+'"')
        shutil.copyfileobj(response.raw, out_file)
    del response
print('Done!')