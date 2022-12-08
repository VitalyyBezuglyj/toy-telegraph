from flask import render_template, url_for, redirect, flash
from toy_telegraph.forms import PostForm
from toy_telegraph import app, mdeditor, MDEditor

@app.route("/", methods=['GET', 'POST'])
@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        flash('Successfully posted!', 'success')
        return redirect(url_for('post'))


    return render_template('post.html', form=form)

@app.route('/post_2')
def post_2():
    return render_template('post_2.html')
