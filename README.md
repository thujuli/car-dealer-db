# DATABASE DESIGN FOR USED CAR DEALERS

## Backgound

This my final project for RDMS using PostgreSQL.....

## Objective

- Create database design for used car dealers
- Implement database design to database server
- Create and input dummy data for each table
- Test Backup and restore database
- Creating Transactional Query and Analytical Query

## Requirements

- PostgreSQL
- PostgreSQL Client (psql, DBeaver, pgAdmin etc)
- Python3

## Create Database Design

### Entities and Attributes

![Entities and Attributes](images/entities-attributes.png?raw=true "Entities and Attributes")

### Relations

- Seller can sell more than one Car
- Seller can advertise the Car
- One Car has only one Ad
- Buyer can bid more than one Ad
- Buyers and Sellers can have the same Domicili

### Table Structure and Relations

![Table Structure and Relations](images/diagram.png?raw=true "Table Structureand Relations")

### Constraints and Business Rules

#### Cities

##### Constraints

- id: int not null
- name: varchar(255) not null
- latitude: numeric not null
- longitude: numeric not null

##### Business Rules

- All fields cannot be empty

#### Sellers

##### Constraints

- id: serial
- city_id: int not null
- name: varchar(255) not null
- phone: varchar(20) not null
- primary key (id)
- constraint phone_unique unique (phone)

##### Business Rules

- Primary key auto increment
- All fields cannot be empty
- Phone number cannot be the same (unique)

#### Buyers

##### Constraints

- id: serial
- city_id: int not null
- name: varchar(255) not null
- phone: numeric(20) not null
- primary key (id)
- constraint phone_unique unique (phone)

##### Business Rules

- Primary key auto increment
- All fields cannot be empty
- Phone number cannot be the same (unique)

#### Cars

##### Constraints

- id: serial
- seller_id: int not null
- brand: varchar(255) not null
- model: varchar(255) not null
- type: varchar(255) not null
- year: date not null
- price: int not null
- primary key (id)
- constraint price_check check (price > 0)

##### Business Rules

- Primary key auto increment
- All fields cannot be empty
- Price must be greater than 0

#### Ads

##### Constraints

- id: serial
- seller_id: int not null
- car_id: int not null
- title: varchar(255) not null
- primary key (id)

##### Business Rules

- Primary key auto increment
- All fields cannot be empty

#### Bids

##### Constraints

- create type status as enum ('sent', 'cancel')
- id: serial
- buyer_id: int not null
- ad_id: int not null
- date: date not null
- price: int not null
- status: status not null
- primary key (id)
- constraint price_check check (price > 0)

##### Business Rules

- Primary key auto increment
- All fields cannot be empty
- Price must be greater than 0
- Status must be sent or cancel

## Implementation To The Database Server
