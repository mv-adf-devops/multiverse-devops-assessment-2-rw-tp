from extract import read_csv

def main():
    filename = 'results.csv'
    data = read_csv(filename)
    print(data)


if __name__ == "__main__":
    main()