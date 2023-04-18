from flask import Flask
import random

app = Flask(__name__)

# topics = [
#     {'id':1, 'title':'html', 'body':'html is...'},
#     {'id':2, 'title':'css', 'body':'css is...'},
#     {'id':3, 'title':'javascript', 'body':'javascript is...'}
# ]


@app.route('/')
def index():
    return 'hi'
    # liTags = ''
    # for topic in topics:
    #     liTags = liTags + f'<li>{topic["title"]}</li>'
    # return  f'''<!doctype html>
    # <html>
    #     <body>
    #         <h1><a href="/">WEB</a></h1>
    #         <ol>
    #             {liTags}
    #         </ol>
    #         <h2>Welcome</h2>
    #         Hello, Web
    #     </body>
    # </html> 복붙 대마왕임 ㄹㅇ 하나 배웠다 ㅋㅋ
    # '''

@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/<ab>')
def read(ab):
    print(ab)
    return 'Read '+ab

if __name__ == "__main__":
    app.run(port=5001)

