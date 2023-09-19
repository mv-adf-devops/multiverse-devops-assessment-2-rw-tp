from extract import read_csv
import os

def main():
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    filename = absolute_path + '/results.csv'
    data = read_csv(filename)
    print(data)

if __name__ == "__main__":
    main()