from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import random

app = Flask(__name__)
app.secret_key = 'https://shiny-spork-44vr4w74p4727xr.github.dev/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_warehouseadmin_data.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(100), nullable=False)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    庫存 = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()

    if not User.query.filter_by(username='root').first():
        password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10))
        print(f"Generated random password for root user: {password}")
        hashed_password = generate_password_hash(password)
        admin_user = User(username='root', password=hashed_password, name='管理員')
        db.session.add(admin_user)
        db.session.commit()

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    items = Item.query.all()
    return render_template('dashboard.html', items=items)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    if user.username != 'root':
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        action = request.form.get('action')


        if action == 'add_user':
            new_username = request.form['new_username']
            new_password = request.form['new_password']
            name = request.form['name']
            if User.query.filter_by(username=new_username).first() is None:
                hashed_password = generate_password_hash(new_password)
                new_user = User(username=new_username, password=hashed_password, name=name)
                db.session.add(new_user)
                db.session.commit()
                flash('用戶添加成功！', 'success')
            else:
                flash('用戶名已存在。', 'danger')
        

        elif action == 'delete_user':
            user_id_to_delete = request.form['user_id_to_delete']
            user_to_delete = User.query.get(user_id_to_delete)
            if user_to_delete and user_to_delete.username != 'root':
                db.session.delete(user_to_delete)
                db.session.commit()
                flash('用戶刪除成功！', 'success')
            else:
                flash('無法刪除根用戶或用戶未找到。', 'danger')

    users = User.query.all()
    return render_template('admin.html', users=users)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name']
        庫存 = request.form['庫存']
        price = request.form['price']
        new_item = Item(name=name, 庫存=庫存, price=price)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('dashboard'))

    return render_template('add_item.html')

@app.route('/edit_item/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = Item.query.get_or_404(item_id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.庫存 = request.form['庫存']
        item.price = request.form['price']
        db.session.commit()
        flash('物品更新成功！', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('edit_item.html', item=item)

@app.route('/delete_item/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('物品刪除成功！', 'success')
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
