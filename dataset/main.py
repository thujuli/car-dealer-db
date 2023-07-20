from faker import Faker
import random
import csv


def csv_to_list(file_read: str) -> list:
    """
    Read csv file and convert to list of dictionary
    """
    list_of_dict = []

    with open(f"{file_read}.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            list_of_dict.append(row)

    return list_of_dict


def list_to_csv(list_of_dict: list, file_write: str) -> None:
    """
    Write to csv file from list of dictionary
    """
    with open(f"{file_write}.csv", "w") as csv_file:
        fieldnames = [_ for _ in list_of_dict[0]]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        csv_writer.writeheader()
        for row in list_of_dict:
            csv_writer.writerow(row)


def list_of_sellers(n_generated: int, list_of_dict: list) -> list:
    """
    Generate list of dictionary for sellers
    """
    fake = Faker(["id_ID"])
    sellers = []

    # get city_id from city (list of dict)
    city_id = [sample_city[i]["kota_id"] for i in range(len(list_of_dict))]

    for i in range(n_generated):
        # id, city_id, name, phone
        sellers.append(
            {
                "id": i + 1,
                "city_id": random.choice(city_id),
                "name": fake.name(),
                "phone": fake.phone_number(),
            }
        )

    return sellers


if __name__ == "__main__":
    # create list of dict from sample dataset
    sample_city = csv_to_list("sample/city")
    sample_car = csv_to_list("sample/car_product")

    sellers = list_of_sellers(100, sample_city)
    list_to_csv(sellers, "final/sellers")
