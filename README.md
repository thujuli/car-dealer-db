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

### Business Rules

#### Cities

- All fields cannot be empty

#### Sellers

- Primary key auto increment
- All fields cannot be empty
- Phone number cannot be the same (unique)

#### Buyers

- Primary key auto increment
- All fields cannot be empty
- Phone number cannot be the same (unique)

#### Cars

- Primary key auto increment
- All fields cannot be empty
- Price must be greater than 0

#### Ads

- Primary key auto increment
- All fields cannot be empty

#### Bids

- Primary key auto increment
- All fields cannot be empty
- Price must be greater than 0
- Default date is current date
- Status must be sent or cancel
- Default status is sent

## Implementation To The Database Server

#### Connect to PostgreSQL Client (psql)

```
# example create connection to database postgres
psql --username=postgres --dbname=postgres --password
```

#### Create database for store all tables

```sql
CREATE DATABASE car-dealer;
```

#### Exit from PostgreSQL Client (psql)

```
exit
```

#### Create all tables from sql script

```
psql --username=postgres --dbname=car-dealer --password --file=sql/ddl.sql
```

#### Connect to new database

```
psql --username=postgres --dbname=car-dealer --password
```

#### Checks all tables already exists

```
\dt
```
