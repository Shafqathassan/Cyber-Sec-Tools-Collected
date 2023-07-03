import requests

x = requests.get('http://httpbin.org/get')

print(x.headers)
print(x.headers['Server'])
print(x.status_code)

if x.status_code == 200:
    print("Sucess")
elif x.status_code == 404:
    print("Not Found ! ")
    
print(x.elapsed)
print(x.cookies)
print(x.ccokies)
print(x.text)


x = requests.get('http://httpbin.org/get', params = {'id' : '1'})
print(x.url)


x = requests.get('http://httpbin.org/get?id =2')
print(x.url)


x = requests.get('http://httpbin.org/get', params = {'id' : '3'}, headers = {'Accept' : 'application.json', 'testheader' : 'test' })
print(x.text)


x = requests.delete('http://httpbin.org/delete')
print(x.text)


x = requests.post('http://httpbin.org/post', data = {'a': 'b' } )
print(x.text)

#to upload data
files= {'file' : open ('google.png' , 'rb' ) }


x = requests.post('http://httpbin.org/post', files = files)
print(x.text)

#to handle basic authentication


x = requests.get('http://httpbin.org/get', auth = ('username', 'password'))
print(x.text)


x = requests.get('http://expired.badssl.com')
print(x.text)

x = requests.get('http://expired.badssl.com', verify = False)
print(x.text)

#Control redirects


x = requests.get('http://github.com')
print(x.headers)

x = requests.get('http://httpbin.org/get', timeout = 0.01)
print(x.request)

x = requests.get('http://httpbin.org/cookies', cookies = {'a' : 'b'})
print(x.content)

x = requests.Session()
x.cookies(update({'a' : 'b'} ) 
print(x.get('http://httpbin.org/cookies').text())

#pass Json responses as Json
x = requests.get('https://api.github.com/events')
print(x.json())

































