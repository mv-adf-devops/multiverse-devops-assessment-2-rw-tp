from extract import read_csv, print_results
import os

def main():    
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    filename = absolute_path + '/results.csv'
    # data = read_csv(filename)
    print_results(filename)

if __name__ == "__main__":
    main()