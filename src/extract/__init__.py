def read_csv(filename, output_filename='clean_results.csv'):
    rows = []
    try:
        with open(filename, 'r') as f:
            for i, line in enumerate(f.readlines()):
                # Skip empty lines
                if line.strip():
                    row = line.strip().split(',')
                    # Ignore header row
                    if i != 0:
                        #Skip line if answer_30 not between 1 and 10
                        try:
                            answer_3 = int(row[5])
                            if answer_3 < 1 or answer_3 > 10:
                                continue
                        except ValueError:
                                continue
                        # Capitalize first_name and last_name
                        row[1] = row[1].capitalize()
                        row[2] = row[2].capitalize()

                    rows.append(row)
                    
        # Remove duplicates
        rows = remove_duplicates(rows)

        # Write the cleansed data to a new CSV file
        with open(output_filename, 'w') as f:
            for row in rows:
                f.write(','.join(row) + '\n')
    # except FileNotFoundError as e:
    except OSError as e:
        print(e)                     
    return rows 

def remove_duplicates(data):    
    unique_data = []
    for row in data:
        if row[0] not in [r[0] for r in unique_data]:
            unique_data.append(row)
    return unique_data

def print_results(filename='results.csv', fixed_length=False):
    rows = read_csv(filename)
    if fixed_length:
        # Find maximum length for each column for formatting
        max_lengths = [max(len(str(item)) + 1 for item in col) for col in zip(*rows)]
        
        # Print each row with fixed-length formatting
        for row in rows:
            print(''.join([str(item).ljust(max_lengths[i]) for i, item in enumerate(row)]))
    else:
        # Print each row normally
        for row in rows:
            print(', '.join(row))

if __name__ == '__main__':
    print_results(fixed_length=True)