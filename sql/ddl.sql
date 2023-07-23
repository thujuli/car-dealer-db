CREATE TABLE cities
(
	id int NOT NULL,
	name varchar(255) NOT NULL,
	latitude NUMERIC NOT NULL,
	longitude NUMERIC NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE sellers
(
	id serial,
	city_id int NOT NULL,
	name varchar(255) NOT NULL,
	phone varchar(255) NOT NULL,
	PRIMARY KEY (id),
	CONSTRAINT fk_city_seller FOREIGN KEY (city_id) REFERENCES cities(id),
	CONSTRAINT seller_phone_unique UNIQUE (phone)
);

CREATE TABLE buyers 
(
	id serial,
	city_id int NOT NULL,
	name varchar(255) NOT NULL,
	phone varchar(255) NOT NULL,
	PRIMARY KEY (id),
	CONSTRAINT fk_city_buyer FOREIGN KEY (city_id) REFERENCES cities(id),
	CONSTRAINT buyer_phone_unique UNIQUE (phone)
);

CREATE TABLE cars
(
	id serial, 
	seller_id int NOT NULL,
	brand varchar(255) NOT NULL,
	model varchar(255) NOT NULL,
	type varchar(255) NOT NULL,
	year int NOT NULL,
	price int NOT NULL,
	PRIMARY KEY (id),
	CONSTRAINT fk_seller_car FOREIGN KEY (seller_id) REFERENCES sellers (id),
	CONSTRAINT price_check CHECK (price > 0)
);

CREATE TABLE ads 
(
	id serial, 
	car_id int NOT NULL,
	title varchar(255) NOT NULL,
	date date NOT NULL DEFAULT current_date,
	PRIMARY KEY (id),
	CONSTRAINT fk_car_ad FOREIGN KEY (car_id) REFERENCES cars (id)
);

CREATE TYPE status AS ENUM ('sent', 'cancel');

CREATE TABLE bids
(
	id serial, 
	buyer_id int NOT NULL,
	ad_id int NOT NULL,
	date date NOT NULL DEFAULT current_date,
	price int NOT NULL,
	status status DEFAULT 'sent' NOT NULL,
	PRIMARY KEY (id),
	CONSTRAINT fk_buyer_bid FOREIGN KEY (buyer_id) REFERENCES buyers (id),
	CONSTRAINT fk_ad_bid FOREIGN KEY (ad_id) REFERENCES ads (id),
	CONSTRAINT price_check CHECK (price > 0)
);
