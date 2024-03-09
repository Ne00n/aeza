# aeza

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
pip3 install pyppeteer
apt-get -y install chromium-browser
cp config.example.json config.json
```

**Chromium**<br />
You may have to edit "executablePath" in the config.json</br>