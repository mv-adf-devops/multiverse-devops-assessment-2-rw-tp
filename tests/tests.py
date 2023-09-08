from extract import read_csv, remove_duplicates

'''
Ticket #1 Read a CSV file
Description In your input script, create a function that will read data from a CSV file.
Objectives 
● The results.csv data file can be successfully processed into an array.
● Each line of the file is read into a new array item.
● The file read method must be in a sub-module.
'''

def test_file_read_to_list():
    #Arrange
    filename = 'results.csv'
    expected_output = list

    #Act
    output = read_csv(filename)

    #Assert
    assert type(output) == expected_output

def test_header_is_correct():
    #Arrange
    filename = 'results.csv'    
    expected_output = ['user_id','first_name','last_name','answer_1','answer_2','answer_3']

    #Act
    output = read_csv(filename)

    #Assert
    assert output[0] == expected_output

def test_incorrect_filename():
    #Arrange
    filename = 'wrong_filename.csv'
    expected_output = list

    #Act
    output = read_csv(filename)

    #Assert
    assert type(output) == expected_output    


'''
Ticket #2 Remove duplicate entries
Description Add functionality to your input script to ignore or remove any duplicate entries
from the input data.
Duplicates are based on the User Id field.
Objectives 
● A final array is created with duplicate entries removed.
● Where duplicates are found, the first entry is retained.
'''    

def test_duplicates_removed():
    #Arrange
    filename = 'results.csv'
    data = read_csv(filename)    
    expected_output = [['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3'], ['1', 'Charissa', 'Clark', 'yes', 'c', '7'], 
    ['2', 'richard', 'McKinney', 'yes', 'b', '7'], ['', '', '', '', '', ''], ['3', 'patience', 'reeves', 'yes', 'b', '9'], 
    ['4', 'Harding', 'Estrada', 'no', 'b', '14'], ['5', 'India', 'Gentry', 'yes', 'c', '7'], ['6', 'Abra', 'Sheppard', 'yes', 'b', '6'], 
    ['7', 'Bryar', 'cooley', 'yes', 'a', '11'], ['8', 'Diana', 'Cameron', 'yes', 'b', '9'], ['9', 'Alexander', 'Herring', 'no', 'b', '4'], 
    ['10', 'Graiden', 'Cannon', 'no', 'b', '13'], ['11', 'Uma', 'Glass', 'yes', 'a', '2'], ['12', 'Brittany', 'Weeks', 'yes', 'b', '8'], 
    ['13', 'Roth', 'Stout', 'yes', 'c', '10'], ['14', 'Amos', 'Daniel', 'yes', 'a', '5'], ['15', 'Caesar', 'Rivers', 'yes', 'b', '7'], 
    ['16', 'Eugenia', 'Nichols', 'yes', 'b', '6'], ['17', 'dieter', 'alvarado', 'yes', 'b', '6'], ['18', 'Roary', 'Frank', 'yes', 'c', '7'], 
    ['19', 'Ulric', 'Hensley', 'no', 'b', '9'], ['20', 'Felicia', 'Wilkins', 'yes', 'b', '8']]

    #Act
    data = remove_duplicates(data)

    #Assert
    assert data == expected_output

