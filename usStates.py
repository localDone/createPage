
import glob
import os
import csv
import pandas as pd

def create_csv():
    try:
        file_path = 'D:\\usNumbers\\'
        # Closes the HTML file
        with open('{0}\\statesDone\\allStates.csv'.format(file_path), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Coutry", "City", "Carrier", "Number", "Letus Type", "Expected Type", "Error Message", "State"])
        # Create Folder links
        for raw_file_name in glob.glob(os.path.join(file_path, '*.csv')):
            print(raw_file_name)
            state = raw_file_name.split('\\')[len(raw_file_name.split('\\')) - 1].split('.')[0]
            with open(raw_file_name, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in spamreader:
                    print(' '.join(row).split(','))
                    arr = ' '.join(row).split(',')

                    coutry = arr[0]
                    city = arr[1]
                    carrier = arr[2]
                    number = arr[3]
                    letusType = arr[4]
                    expectedType = arr[5]
                    errorMessage = arr[6]
                    with open('{0}\\statesDone\\allStates.csv'.format(file_path), 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(
                            [coutry, city, carrier, number, letusType, expectedType, errorMessage,
                             state])
                    # print(', '.join(row))

        # f.write(page_bottom)
        # f.close()

    except Exception as e:
        print("Error while creating page", e)

    finally:
        print('Done')
        # f.close()
        # print("End of Create_Page")



def create_csv1():
    try:
        file_path = 'D:\\usNumbers\\'
        # Closes the HTML file
        with open('{0}\\statesDone\\allStates.csv'.format(file_path), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Coutry", "City", "Carrier", "Number", "Letus Type", "Expected Type", "Error Message", "State"])
        # Create Folder links
        for raw_file_name in glob.glob(os.path.join(file_path, '*.csv')):
            print(raw_file_name)
            state = raw_file_name.split('\\')[len(raw_file_name.split('\\')) - 1].split('.')[0]
            df = pd.read_csv(raw_file_name)
            # print(df.to_string())
            for i in df.to_string().split('\n'):
                print(i)
        # f.write(page_bottom)
        # f.close()

    except Exception as e:
        print("Error while creating page", e)

    finally:
        print('Done')
        # f.close()
        # print("End of Create_Page")

create_csv1()