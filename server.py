from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

posts = []


class Posts(Resource):
    def get(self, postId):
        for post in posts:
            if post['id'] == postId:
                return post
        return {'post': None}, 404

    def post(self):
        post = {'id': 1, 'title': 'New article',
                'description': 'article description'}
        posts.append(post)
        return post, 201


api.add_resource(Posts, '/posts')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
