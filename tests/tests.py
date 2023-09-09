from extract import read_csv, remove_duplicates, print_results

'''
Ticket #1 Read a CSV file
Description: 
In your input script, create a function that will read data from a CSV file.
Objectives:
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
Description: 
Add functionality to your input script to ignore or remove any duplicate entries
from the input data. Duplicates are based on the User Id field.
Objectives:
● A final array is created with duplicate entries removed.
● Where duplicates are found, the first entry is retained.
'''    

def test_duplicates_removed():
    #Arrange
    input_file = "tests/data//test_2_input.csv"
    output_file = "tests/data/test_2_exp_output.csv"
    input_data = read_csv(input_file)
    exp_output_data  = read_csv(output_file)

    #Act
    data = remove_duplicates(input_data)

    #Assert
    assert data == exp_output_data

'''
Ticket #3 Ignore empty lines
Description: 
Update your input script to ignore any empty lines found when reading in the input data file.
Objectives: 
● A final array is created with any empty lines omitted
'''

def test_ignore_empty_lines():
    # Arrange
    input_file = "tests/data/test_3_input.csv"
    output_file = "tests/data/test_3_exp_output.csv"   
    
    # Act
    input_data = read_csv(input_file)
    exp_output_data = read_csv(output_file)
    
    # Assert
    assert input_data == exp_output_data

'''
Ticket #4 Capitalise user name fields
Description: 
Add functionality to your input script to automatically capitalise the first_name
and last_name fields found in the input data.
Objectives: 
● All names are capitalised in all data entries.
'''

def test_capitalize_names():
    # Arrange
    input_file = "tests/data/test_4_input.csv"
    output_file = "tests/data/test_4_exp_output.csv"   
    
    # Act
    input_data = read_csv(input_file)
    exp_output_data = read_csv(output_file)
    
    # Assert
    assert input_data == exp_output_data

'''
Ticket #5 Validate the responses to answer 3
Description: 
Update your input script to validate the responses to the third answer field.
This answer must have a numeric value between 1 and 10. Any rows with an invalid value are ignored.
Objectives: 
● A final array is created with the input data excluding any rows where answer 3 is invalid.
● No answer 3 values will be outside the range of 1 to 10.
'''

def test_validate_answer_3():
    # Arrange
    input_file = "tests/data/test_5_input.csv"
    output_file = "tests/data/test_5_exp_output.csv"   
    
    # Act
    input_data = read_csv(input_file)
    exp_output_data = read_csv(output_file)

    # Assert
    assert input_data == exp_output_data



'''
Ticket #6 Output the cleansed result data to a new file
Description: 
Add functionality to your input script to output the cleansed data to a new CSV file.
Objectives: 
● A new file is created called clean_results.csv.
● The file is recreated on each execution.
● No invalid or unformatted data is present in the new file.
'''

def test_clean_data_to_file():
    # Arrange
    input_file = "tests/data/test_6_input.csv"
    output_file = "tests/data/test_6_exp_output.csv"
    test_output_filename = 'test_clean_results.csv'
    
    # Act
    read_csv(input_file, test_output_filename)
    
    # Assert
    try:
        with open(test_output_filename, 'r') as f:
            lines = f.readlines()
            output = [line.strip().split(',') for line in lines]
        with open(output_file, 'r') as f:
            lines = f.readlines()
            expected_output = [line.strip().split(',') for line in lines]                    
        assert output == expected_output
    except FileNotFoundError:
        assert False, "File not available."

'''
Ticket #7 Create an output script
Description: 
A new output script will be created which reads in the clean_results.csv CSV
file and outputs the results to the command line, row by row.
Objectives: 
● The script uses the existing sub-module to read the CSV file.
● The printed output will contain all row data and an appropriate header.
● Stretch: The printed output will be formatted with fixed length strings.
'''

def test_print_clean_results(capsys):
    # Arrange
    input_file = "tests/data/test_7_input.csv"
    save_filename = 'sample_clean_results.csv'
    read_csv(input_file, save_filename)

    expected_output_default = """user_id, first_name, last_name, answer_1, answer_2, answer_3
1, Charissa, Clark, yes, c, 7
2, Richard, Mckinney, yes, b, 7
3, Patience, Reeves, yes, b, 9
"""
    expected_output_fixed_length = """user_id first_name last_name answer_1 answer_2 answer_3 
1       Charissa   Clark     yes      c        7        
2       Richard    Mckinney  yes      b        7        
3       Patience   Reeves    yes      b        9        
"""
    # Act and Assert for default mode
    print_results(save_filename)
    captured = capsys.readouterr()
    assert captured.out == expected_output_default
    
    # Act and Assert for fixed-length mode
    print_results(save_filename, fixed_length=True)
    captured = capsys.readouterr()
    assert captured.out == expected_output_fixed_length

