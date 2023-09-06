from extract import read_csv

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