from utils import get_data, get_filtered_data, get_last_values


def main():
    data = get_data()
    data = get_filtered_data(data)
    data = get_last_values(data)

if __name__ == "__main__":
    main()