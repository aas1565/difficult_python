import re
import sqlite3
from forms import MyForm
from flask import Flask, render_template, request, redirect, url_for
from typing import List, Dict

from models import init_db, DATA, get_all_books, Book

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)

BOOKS = [
    {'id': 0, 'title': 'A byte of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 2, 'title': 'Mar and Peace', 'author': 'Lev Tolstoy'},
]

def _get_hmtl_table_for_books(books: List[Dict]) -> str:
    table = """
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Title</th>
                    <th>Author</th>
                </tr>
            </thead>
                <tbody>
                    {books_rows}
                </tbody>
        </table>
    """
    rows = ''
    for book in books:
        rows += '<tr><td>{id}</tb><td>{title}</tb><td>{author}</tb></tr>'.format(
            id=book['id'], title=book['title'], author=book['author'],
        )
    return table.format(books_rows=rows)

def add_book_to_db(data):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO table_books (title, author) VALUES (?, ?)', data)
        conn.commit()


def get_books_by_author(author):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM table_books WHERE author = ?', (author,))
        books_by_author = cursor.fetchall()

    #return _get_hmtl_table_for_books(books_by_author)
    return books_by_author


@app.route('/author/<author>')
def author_books(author):
    table = get_books_by_author(author)
    second_values = [item[1] for item in table]
    return second_values


@app.route('/pred')
def red_index():
    return render_template('pred_index.html', books=get_all_books())


@app.route('/books', methods=['GET', 'POST'])
def books():
    form=MyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            data = form.title.data, form.author.data
            add_book_to_db(data)
            return redirect('/pred')

    books = get_all_books()
    return render_template('add_book.html', form=form)

if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
