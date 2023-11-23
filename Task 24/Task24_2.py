# CREATE TABLE Task24_2(book_id int, book_title text, book_author text, publisher_id int, price int, count int)
# insert into Task24_2 values
# (1, 'Великий Гэтсби', 'Фрэнсис Скотт Фицджеральд', 100, 256),
# (2, 'Мастер и Маргарита', 'Михаил Булгаков', 101, 448),
# (13, 'Собачье сердце', 'Михаил Булгаков', 101, 243),
# (13, 'Морфий', 'Михаил Булгаков', 101, 332),
# (3, '1984', 'Джордж Оруэлл', 100, 328),
# (14, 'Скотный двор', 'Джордж Оруэлл', 100, 289),
# (4, 'Тысяча великих солнц', 'Халед Хоссейни', 100, 384),
# (5, 'Гарри Поттер и философский камень', 'Дж. К. Роулинг', 101, 320),
# (10, 'Мартин Иден', 'Джек Лондон', 100, 448),
# (11, 'Фауст', 'Иоганн Вольфганг фон Гёте', 100, 448),
# (12, 'Гарри Поттер и Дары Смерти', 'Дж. К. Роулинг', 100, 784)
#
# CREATE VIEW author_books_count AS
# SELECT book_author, COUNT(*) AS books_count
# FROM Task24_2
# GROUP BY book_author;
#
# select * from author_books_count
#
# SELECT abc.book_author, abc.books_count
# FROM author_books_count abc
# WHERE abc.books_count = (SELECT MIN(books_count) FROM author_books_count);
