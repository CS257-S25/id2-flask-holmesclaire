'''file: loadData.py'''
import csv

def load_data():
    ''' Purpose: Load data from a file
    Returns: None'''
    print("Loading data from file...")
    #this loads the data needed for get_top_by_age.py 
    with open("Data/mini_data_set_for_testing.csv", "r") as file:
        reader=csv.DictReader(file)
        data = list(reader)
        return data
    
def load_categories():
    '''Purpose: loads category IDs and their category
    Returns: None
    '''
    with open("Data/Categories_Data.csv", "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)
        return data

def main():
    cat = load_categories()
    print(cat)

if __name__ == "__main__":
    main()
