create schema `db_hw2`;
use db_hw2;

create table authors(
	auth_id int primary key auto_increment,
	name varchar(100) not null
);

create table publishers(
	pub_id int primary key auto_increment,
	name varchar(100) not null
);

create table books(
	book_id int primary key auto_increment,
	title varchar(255) not null,
	publisher int,
	foreign key(publisher) references publishers(pub_id)
);

create table wrote(
	author int,
    book int,
    primary key (author,book),
    foreign key(author) references authors(auth_id),
    foreign key(book) references books(book_id)

);
