def read_csv(filename):
    rows = []
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                rows.append(line.strip().split(','))
    # except FileNotFoundError as e:
    except OSError as e:
        print(e)
        #raise                
    return rows    
    #return []

def remove_duplicates(data):    
    unique_data = []
    for row in data:
        if row[0] not in [r[0] for r in unique_data]:
            unique_data.append(row)
    return unique_data