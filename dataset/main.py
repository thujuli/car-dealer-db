from function.csv_list import csv_to_list, list_to_csv
from function.generate_list import (
    list_of_city,
    list_of_users,
    list_of_car,
    list_of_ads,
    list_of_bids,
)


if __name__ == "__main__":
    # create list of dict from sample dataset
    sample_city = csv_to_list("sample/city")
    sample_car = csv_to_list("sample/car_product")

    cities = list_of_city(sample_city)
    sellers = list_of_users(10, cities)
    buyers = list_of_users(15, cities)
    cars = list_of_car(sample_car, sellers)
    ads = list_of_ads(10, sellers, cars)
    bids = list_of_bids(10, buyers, ads)

    list_to_csv(cities, "final/cities")
    list_to_csv(buyers, "final/buyers")
    list_to_csv(sellers, "final/sellers")
    list_to_csv(cars, "final/cars")
    list_to_csv(ads, "final/ads")
    list_to_csv(bids, "final/bids")
