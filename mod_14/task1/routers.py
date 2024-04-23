import re
import sqlite3
from forms import MyForm
from flask import Flask, render_template, request, redirect, url_for
from typing import List, Dict

from models import init_db, DATA, get_all_books, Book

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

def add_book_to_db(title: str, author: str):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO table_books (title, author) VALUES (?, ?)', (title, author))
        conn.commit()

@app.route('/pred')
def red_index():
    return render_template('pred_index.html', books=get_all_books())


@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        add_book_to_db(title, author)
        return redirect('/pred')

    books = get_all_books()
    return render_template('add_book.html', books=books)





if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
