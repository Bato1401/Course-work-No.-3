from utils import get_data, get_filtered_data, get_last_values, get_data_output


def main():
    data = get_data()
    data = get_filtered_data(data)
    data = get_last_values(data)
    data = get_data_output(data)
    for row in data:
        print(row, end='\n\n')


if __name__ == "__main__":
    main()
