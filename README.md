# aeza

![outplayed](https://i.pinimg.com/originals/f2/8c/57/f28c57e6bfa870458242641fb81ff8d1.gif)

## Work in Progress

```
curl 'https://my.aeza.net/api/services/mahServiceID/ctl?' --compressed -X POST 
-H 'Accept: application/json' -H 'Referer: https://my.aeza.net/services/mahServiceID/' 
-H 'Content-Type: application/json' -H 'Authorization: Bearer mahCookey' 
-H 'Origin: https://my.aeza.net' -H 'Cookie: token=mahCookey' --data-raw '{"action":"resume"}
```

**Dependencies**<br />
Python 3.7 or higher<br />
```
pip3 install pyppeteer PyVirtualDisplay fake-useragent
apt-get -y install chromium-browser xvfb
cp config.example.json config.json
```

**Chromium**<br />
You may have to edit "executablePath" in the config.json</br>