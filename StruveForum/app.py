from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


forum_posts = []

opinions = {}

@app.route('/')
def index():
    return render_template('index.html', posts=forum_posts)

@app.route('/submit_post', methods=['POST'])
def submit_post():
    if request.method == 'POST':
        post_title = request.form['post_title']
        post_content = request.form['post_content']
        post = {'title': post_title, 'content': post_content}
        forum_posts.append(post)
        opinions[len(forum_posts) - 1] = []  
    return redirect(url_for('index'))

@app.route('/submit_opinion/<int:post_id>', methods=['POST'])
def submit_opinion(post_id):
    if request.method == 'POST':
        opinion_content = request.form['opinion_content']
        opinions[post_id].append(opinion_content)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)