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