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

![Entities and Attributes](diagram/images/entities-attributes.png?raw=true "Entities and Attributes")

### Relations

- One City can have many Users (Sellers and Buyers)
- One Seller can own many Cars
- One Car can have many Ads
- One Buyer can bid many Ads
- One Advertisment offered be many Buyers

### Table Structure and Relations

![Table Structure and Relations](diagram/images/diagram.png?raw=true "Table Structure and Relations")

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

## Setup Project

#### Clone this repository

```bash
# clone using ssh
git clone git@github.com:thujuli/car-dealer-db.git

# clone using https
git clone https://github.com/thujuli/car-dealer-db.git
```

#### Change directory to this repository

```bash
cd car-dealer-db/
```

## Implementation To The Database Server

#### Create new database using psql

```bash
psql --username=postgres --command="CREATE DATABASE car_dealer;" --password
```

#### Create all tables from sql script

```bash
psql --username=postgres --dbname=car_dealer --password --file=sql/ddl.sql
```

#### Checks all tables already exists

```bash
psql --username=postgres --dbname=car_dealer --command="\dt" --password
```

## Create And Input Dummy Data For Each Table

#### Create virtual environment

```bash
python -m venv .venv
```

#### Use the virtual environment

```bash
source .venv/bin/activate
```

#### Install third party packages from requirements.txt

```bash
pip install -r requirements.txt
```

#### Change directory to dataset

```bash
cd dataset/
```

#### Run python script

```bash
python main.py
```

#### Checks all created csv files

```bash
ls final/
```

#### Import csv files (dummy data) for each table

```bash
# import for table cities
psql --username=postgres --dbname=car_dealer --command="\copy cities from 'final/cities.csv' delimiter ',' csv header" --password

# import for table sellers
psql --username=postgres --dbname=car_dealer --command="\copy sellers from 'final/sellers.csv' delimiter ',' csv header" --password

# import for table buyers
psql --username=postgres --dbname=car_dealer --command="\copy buyers from 'final/buyers.csv' delimiter ',' csv header" --password

# import for table cars
psql --username=postgres --dbname=car_dealer --command="\copy cars from 'final/cars.csv' delimiter ',' csv header" --password

# import for table ads
psql --username=postgres --dbname=car_dealer --command="\copy ads from 'final/ads.csv' delimiter ',' csv header" --password

# import for table bids
psql --username=postgres --dbname=car_dealer --command="\copy bids from 'final/bids.csv' delimiter ',' csv header" --password
```

#### Test queries to each table

```bash
# queries table cities
psql --username=postgres --dbname=car_dealer --command="select * from cities;" --password

# queries table sellers
psql --username=postgres --dbname=car_dealer --command="select * from sellers;" --password

# queries table buyers
psql --username=postgres --dbname=car_dealer --command="select * from buyers;" --password

# queries table cars
psql --username=postgres --dbname=car_dealer --command="select * from cars;" --password

# queries table ads
psql --username=postgres --dbname=car_dealer --command="select * from ads;" --password

# queries table bids
psql --username=postgres --dbname=car_dealer --command="select * from bids;" --password
```

#### Back to main directory

```bash
cd ..
```

## Test Backup And Restore Database

#### Backup database
