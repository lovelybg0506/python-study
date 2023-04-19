from flask import Flask, request, redirect
import random

app = Flask(__name__)


nextId = 4
topics = [
    {'id':1, 'title':'html', 'body':'html is...'},
    {'id':2, 'title':'css', 'body':'css is...'},
    {'id':3, 'title':'javascript', 'body':'javascript is...'}
]

def template(contents, content):
    return  f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href="/create/">create</a></li>
            </ul>
        </body>
    </html>
    '''

def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

@app.route('/')
def index():
    return  template(getContents(), '<h2>Welcome</h2>Hello, WEB')

@app.route('/create/', methods=['GET','POST'])
def create():
    # print('request.method : ', request.method) # 요청한것이 GET인지 POST인지 확인
    if request.method == 'GET':
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><input type="password" name="password" placeholder="pwd"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id':nextId, 'title':title, 'body':body}
        topics.append(newTopic)
        # url = '/read/'+str(nextId)+'/'
        url = '/read/{0}/'.format(nextId)
        print("url : " + url)
        nextId = nextId + 1
        return redirect(url)

@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    print(title,body)
    return  template(getContents(), f'<h2>{title}</h2>{body}')

if __name__ == "__main__":
    app.run(port=5001, debug=True)

