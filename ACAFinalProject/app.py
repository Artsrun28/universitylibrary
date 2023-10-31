from flask import Flask, render_template, redirect, request, url_for, session
import glob
import os
from forms import CreateBookForm, LoginForm, RegisterForm

from models.books import Book
from models.user import User
from login import login_required

app = Flask(__name__, static_url_path='/media')
app.config.from_object("config.AppConfig")


@app.context_processor
def inject_data():
    user_id = session.get("user")
    user = None
    if user_id:
        user = User.get(user_id)
    return {"user": user}


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.get(username=form.username.data)
        hashed_password = User.hash_password(form.username.data, form.password.data)
        if not user or user.password != hashed_password:
            form.username.errors.append('Invalid credentials')
            render_template("login.html", form=form)
        session['user'] = user.id
        return_url = request.args.get("next")
        return redirect(return_url if return_url else "/")
    return render_template(template_name_or_list="login.html", form=form)


@app.route('/logout')
def logout():
    session['user'] = None
    return redirect('/login')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.from_registration_form(form)
        user.save()
        return redirect("/our-students")
    return render_template(template_name_or_list="register.html", form=form)


@app.route('/')
def home():
    return render_template(template_name_or_list='home.html')


@app.route('/about')
def about():
    return render_template(template_name_or_list='about.html')


@app.route('/books')
def books():
    books = Book.select()
    return render_template(template_name_or_list='books.html', books=books)

# Dynamic routing
@app.route('/books/<int:book_id>')
def books_details(book_id):
    try:
        book = Book.get(id=book_id)
        return render_template('books_details.html', book=book)
    except Book.DoesNotExist:
        return render_template(template_name_or_list='404.html'), 404

#app.route decorators methods by default are GET, if you need POST, you need to define methode
@app.route('/books/new', methods=['GET', 'POST'])
@login_required
def new_book():
    create_book_form = CreateBookForm()
    if create_book_form.validate_on_submit():
        book = Book(
            book_name=create_book_form.book_name.data,
            author_name=create_book_form.author_name.data,
            release_year=create_book_form.release_year.data,
            book_copy=create_book_form.book_copy.data,
        )
        book.save()
        return redirect('/books')
    return render_template(template_name_or_list="new_book.html", form=create_book_form)


@app.route('/book_update', methods=['POST'])
def book_update():
    book_id = request.form.get('book_update_id')
    new_book_name = request.form.get('new_book_name')
    author_name = request.form.get('author_name')
    new_release_year = request.form.get('new_release_year')

    if book_id and new_book_name and author_name and new_release_year:
        try:
            book = Book.get(Book.id == book_id)
            book.book_name = new_book_name
            book.author_name = author_name
            book.release_year = new_release_year
            book.save()
        except User.DoesNotExist:
            pass  # Book not found
    return redirect("/books")


@app.route('/delete-book', methods=['POST'])
def delete_book():
    book_id = request.form.get('book_id')
    if book_id:
        try:
            book = Book.get(Book.id == book_id)
            book.delete_instance()
        except Book.DoesNotExist:
            pass  # Book not found
    return redirect("/books")


@app.route('/our-students')
def students():
    students = User.select()
    return render_template(template_name_or_list='students.html', students=students)

# Dynamic routing
@app.route('/students/<int:user_id>')
def student_details(user_id):
    try:
        user = User.get(id=user_id)
        return render_template("student_details.html", user=user)
    except User.DoesNotExist:
        return render_template(template_name_or_list="404.html"), 404


@app.route('/user_update', methods=['POST'])
def user_update():
    user_id = request.form.get('user_update_id')
    new_username = request.form.get('new_username')
    new_full_name = request.form.get('new_full_name')
    new_email = request.form.get('new_email')

    if user_id and new_full_name and new_email and new_username:
        try:
            user = User.get(User.id == user_id)
            user.username = new_username
            user.full_name = new_full_name
            user.email = new_email
            user.save()
        except User.DoesNotExist:
            pass  # User not found
    return redirect("/our-students")


@app.route('/delete-user', methods=['POST'])
def delete_user():
    user_id = request.form.get('user_id')
    if user_id:
        try:
            user = User.get(User.id == user_id)
            user.delete_instance()
        except User.DoesNotExist:
            pass  # User not found
    return redirect("/our-students")


@app.route('/photos')
def photos():
    all_files = map(os.path.basename, glob.glob(f"{app.static_folder}/*.jpg"))
    photo_urls = []
    for file in all_files:
        photo_urls.append(url_for("static", filename=file))
    return render_template(template_name_or_list="photos.html", photo_urls=photo_urls)


@app.route('/photos/new', methods=['GET', 'POST'])
@login_required
def add_photo():
    if request.method == "POST":
        photo = request.files["photo"]
        photo.save(f"{app.static_folder}/{photo.filename}")
        return redirect("/photos")
    return render_template(template_name_or_list="photos_new.html")


if __name__ == '__main__':
    app.run(port=5000, debug=True)


'''TODO
1.Add function for students to be able to take books, decreasing book copy number
2.UX UI
'''
