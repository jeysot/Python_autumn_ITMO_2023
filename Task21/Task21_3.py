create table book (book_id int, book_title text, book_author text, publisher_id int)
insert into book values
(1, 'Война и мир', 'Лев Толстой', 101),
(2, 'Преступление и наказание', 'Федор Достоевский', 101),
(3, '1984', 'Джордж Оруэлл', 102),
(4, 'Мастер и Маргарита', 'Михаил Булгаков', 101),
(5, 'Гарри Поттер и философский камень', 'Дж. К. Роулинг', 102)
select * from book
select book_title from book where publisher_id = 101
select * from book where book_title like 'В%'