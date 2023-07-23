from faker import Faker
import datetime
import random


def list_of_city(list_of_dict: list) -> list:
    """
    Renaming coloumn from dictionary list of city (sample dataset)
    """

    cities = []

    for i in range(len(list_of_dict)):
        cities.append(
            {
                "id": list_of_dict[i]["kota_id"],
                "name": list_of_dict[i]["nama_kota"],
                "latitude": list_of_dict[i]["latitude"],
                "longitude": list_of_dict[i]["longitude"],
            }
        )

    return cities


def list_of_car(list_of_dict: list, seller_list) -> list:
    """
    Renaming coloumn from dictionary list of city (sample dataset) and coloumn seller_id
    """

    cars = []

    # get id from car_list and seller_list
    seller_id = [seller_list[i]["id"] for i in range(len(seller_list))]

    for i in range(len(list_of_dict)):
        cars.append(
            {
                "id": list_of_dict[i]["product_id"],
                "seller_id": random.choice(seller_id),
                "brand": list_of_dict[i]["brand"],
                "model": list_of_dict[i]["model"],
                "type": list_of_dict[i]["body_type"],
                "year": list_of_dict[i]["year"],
                "price": list_of_dict[i]["price"],
            }
        )

    return cars


def list_of_users(n_generated: int, city_list: list) -> list:
    """
    Generate list of dictionary for users (sellers and buyers)
    """
    fake = Faker(["id_ID"])
    users = []

    # get city_id from city (list of dict)
    city_id = [city_list[i]["id"] for i in range(len(city_list))]

    for i in range(n_generated):
        # id, city_id, name, phone
        users.append(
            {
                "id": i + 1,
                "city_id": random.choice(city_id),
                "name": fake.name(),
                "phone": fake.phone_number(),
            }
        )

    return users


def list_of_ads(n_generated: int, car_list: list) -> list:
    """
    Generate list of dictionary for ads
    """
    fake = Faker(["id_ID"])
    ads = []

    # get id from seller_list (list of dict)
    car_id = [car_list[i]["id"] for i in range(len(car_list))]

    for i in range(n_generated):
        # seller_id_choice = random.choice(seller_id)

        # get car id from car_list
        # car_id_from_seller = []
        # for j in range(len(car_list)):
        #     if car_list[j]["seller_id"] == seller_id_choice:
        #         car_id_from_seller.append(car_list[j]["id"])
        #
        ads.append(
            {
                "id": i + 1,
                "car_id": random.choice(car_id),
                "title": fake.sentence(nb_words=4, variable_nb_words=False),
            }
        )

    return ads


def list_of_bids(n_generated: int, buyer_list: list, ad_list: list) -> list:
    """
    Generate list of dictionary for bids
    """
    bids = []

    # get city_id from city (list of dict)
    buyer_id = [buyer_list[i]["id"] for i in range(len(buyer_list))]
    ad_id = [ad_list[i]["id"] for i in range(len(ad_list))]

    for i in range(n_generated):
        # generate date (range from 2022-10-01 to 2022-11-30)
        start_date = datetime.date(2022, 10, 1)
        end_date = datetime.date(2022, 11, 30)

        num_days = (end_date - start_date).days
        rand_days = random.randint(1, num_days)
        random_date = start_date + datetime.timedelta(days=rand_days)

        # adding dict to list
        bids.append(
            {
                "id": i + 1,
                "buyer_id": random.choice(buyer_id),
                "ad_id": random.choice(ad_id),
                "date": random_date,
                "price": random.randrange(100_000_000, 400_000_000, 25_000_000),
                "status": random.choice(("sent", "cancel")),
            }
        )

    return bids
