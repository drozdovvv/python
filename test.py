import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.executescript("""
    create table person(
        firstname,
        lastname,
        age,
        city,
        street
    );

    create table book(
        title,
        author,
        year
    );

    insert into book(title, author, year)
    values (
        'brightness',
        'Stiven King',
        1977
    );
    """)
