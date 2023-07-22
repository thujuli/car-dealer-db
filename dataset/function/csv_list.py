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
