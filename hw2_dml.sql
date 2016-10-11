use db_hw2;

insert into authors (name)
values
  ('Hector Garcia-Molina'),
  ('Jeffrey D. Ulman'),
  ('Jennifer Widom'),
  ('Thomas H. Cormen'),
  ('Sanjoy Dasgupta')
;

insert into publishers(name)
values
	('Prentice Hall'),
    ('MIT Press'),
    ('McGraw Hill');
    
insert into books(title,publisher)
values
	('Database Systems: The Complete Book',1),
    ('Algorithms',3),
    ('Introduction to Algorithms',2);

insert into wrote(author, book)
values
	(1,1),
    (2,1),
    (3,1),
    (4,3),
    (5,2);