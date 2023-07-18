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

```plantuml
@startuml
entity Cities{
    name: varchar
    latitude: float
    longitude: float
}
entity Sellers{
    name: int
    phone: varchar
}
entity Buyers{
    name: int
    phone: varchar
}
entity Ads{
    title: varchar
}
entity Cars{
    brand: varchar
    model: varchar
    type: varchar
    year: date
    price: int
}
entity Bids{
    date: date
    price: int
    status: enum
}
@enduml
```

### Relations

- Seller can sell more than one Car
- Seller can advertise the Car
- One Car has only one Ad
- Buyer can bid more than one Ad
- Buyers and Sellers can have the same Domicili

### Table Structure, Relations and Constraint (Business Rules)

```plantuml
@startuml

entity Cities{
    * id: int <<generated>>
    --
    * name: varchar
    * latitude: float
    * longitude: float
}
entity Sellers{
    * id: int <<generated>>
    --
    * city_id: int <<FK>>
    * name: int
    * phone: varchar <<unique>>
}
entity Buyers{
    * id: int <<generated>>
    --
    * city_id: int <<FK>>
    * name: int
    * phone: varchar <<unique>>
}
entity Ads{
    * id: int <<generated>>
    --
    * seller_id: int <<FK>>
    * car_id: int <<FK>>
    * title: varchar
}
entity Cars{
    * id: int <<generated>>
    --
    * seller_id: int <<FK>>
    * brand: varchar
    * model: varchar
    * type: varchar
    * year: date
    * price: int
}
entity Bids{
    * id: int <<generated>>
    --
    * buyer_id: int <<FK>>
    * ad_id: int <<FK>>
    * date: date
    * price: int
    * status: enum
}

Cities ||..|{ Sellers
Cities ||..|{ Buyers
Sellers |o..|{ Cars
Sellers |o..|{ Ads
Cars |o..|| Ads
Ads |o..|{ Bids
Buyers |o..|{ Bids

@enduml
```

## Implementation To The Database Server
