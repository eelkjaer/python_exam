import datetime
from modules import eksamen_csv
from modules import eksamen_class
import numpy as np


import sklearn

import sys
import scipy
import matplotlib
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot


def calculate_accepted_days(day, month, year):
    date_of_record = datetime.datetime(year, month, day)
    todays_date = datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)
    result = todays_date - date_of_record

    return result.days


def create_machine_learning(computer_to_use):
    cpu_value = 0
    processor_value = 0
    screen_value = 0
    time_value = 0
    ssd_value = ''

    if computer_to_use.cpu.lower() == 'intel core':
        cpu_value = 1
    elif computer_to_use.cpu == 'Apple M1' or (computer_to_use.cpu == 'Apple m1' or computer_to_use.cpu == 'apple m1'):
        cpu_value = 2

    if computer_to_use.processor == 'i3':
        processor_value = 1
    elif computer_to_use.processor == 'i5':
        processor_value = 2
    elif computer_to_use.processor == 'i7':
        processor_value = 3
    elif computer_to_use.processor == 'i9':
        processor_value = 4
    elif computer_to_use.processor == 'M1 M1' or computer_to_use.processor == 'm1 m1':
        processor_value = 5
    elif computer_to_use.processor == 'M1 Pro' or computer_to_use.processor == 'm1 pro':
        processor_value = 6
    elif computer_to_use.processor == 'M1 Max' or computer_to_use.processor == 'm1 max':
        processor_value = 7

    # if computer_to_use.screen == 13:
    #     screen_value = 1
    # elif computer_to_use.screen == 14:
    #     screen_value = 2
    # elif computer_to_use.screen == 15:
    #     screen_value = 3
    # elif computer_to_use.screen == 16:
    #     screen_value = 4

    date_tokens = computer_to_use.date.split('-')
    day = int(date_tokens[0])
    month = int(date_tokens[1])
    year = int(date_tokens[2])
    days = calculate_accepted_days(day, month, year)
    if days <= 30 & days >= 0:
        time_value = 1

    if "." in computer_to_use.ssd:
        token = computer_to_use.ssd.split(".")[1]
    else:
        token = computer_to_use.ssd

    if int(token) < 256:
        ssd_value = str(token) + ' TB'
    else:
        ssd_value = str(token) + ' GB'

    computer_name = computer_to_use.cpu + ' ' + computer_to_use.processor + ' ' + str(computer_to_use.screen) + '" ' + ssd_value + ' ' + str(computer_to_use.ram) + ' GB'

    return [cpu_value, processor_value, int(computer_to_use.ram), int(token), int(computer_to_use.screen), time_value,
            computer_to_use.price, computer_name]


def create_computers_for_machine_learning(computer_list):
    created_computer_list = []

    for computer in computer_list:
        created_computer_list.append(
            eksamen_class.Computer(computer[1], computer[6], computer[4], computer[5], computer[7], computer[9],
                                   computer[0], computer[2], computer[3]))

    return created_computer_list


def convert_computer_list_to_machine_learning_features(list_of_computers):
    machine_learning_list = []

    for computer in list_of_computers:
        machine_learning_list.append(create_machine_learning(computer))

    return machine_learning_list


def create_machine_learning_set_numpy_format(all_computers_in_list_format):

    # Convert list to Computer objects
    computer_list = create_computers_for_machine_learning(all_computers_in_list_format)
    #print(computer_list)
    #print('Length of computer list: ', len(computer_list))

    # Create ML features and target
    machine_learning_list = convert_computer_list_to_machine_learning_features(computer_list)
    #print('\n')
    #print(machine_learning_list)
    #print('Length of machine learning list: ', len(machine_learning_list))

    # Create unique sets of the list
    list_of_machine_learning_sets = [list(item) for item in set(tuple(row) for row in machine_learning_list)]
    #print('\n')
    #print(list_of_machine_learning_sets)
    print('Length of unique sets: ', len(list_of_machine_learning_sets))

    # Convert sets to Numpy array
    list_of_machine_learning_sets_numpy_array = np.array(list_of_machine_learning_sets)
    print('\n')
    print(list_of_machine_learning_sets_numpy_array)
    return list_of_machine_learning_sets_numpy_array


def support_vector_machines_algorithm(X_train, X_test, Y_train, Y_test):
    print('\n')
    print('----------')
    print('Support Vector Machines (SVM)')
    model = SVC(gamma='auto')

    # Training the system with features and targets
    model.fit(X_train, Y_train)

    # Training score
    score = model.score(X_train, Y_train)
    print('Training data score: ', score)

    # Testing the system
    predictions = model.predict(X_test) # Hvilken kategori test data tilhører
    score = model.score(X_test, Y_test)
    print('Test data score: ', score)


def decision_tree_classifier_algorithm(X_train, X_test, Y_train, Y_test):
    print('\n')
    print('----------')
    print('Classification and Regression Trees (CART)')
    model = DecisionTreeClassifier()

    # Training the system with features and targets
    model.fit(X_train, Y_train)

    # Training score
    score = model.score(X_train, Y_train)
    print('Training data score: ', score)

    # Testing the system
    predictions = model.predict(X_test) # Hvilken kategori test data tilhører
    score = model.score(X_test, Y_test)
    print('Test data score: ', score)


def k_nearestn_eighbors_algorithm(X_train, X_test, Y_train, Y_test):
    print('\n')
    print('----------')
    print('K-Nearest Neighbors (KNN)')
    model = KNeighborsClassifier()

    # Training the system with features and targets
    model.fit(X_train, Y_train)

    # Training score
    score = model.score(X_train, Y_train)
    print('Training data score: ', score)

    # Testing the system
    predictions = model.predict(X_test) # Hvilken kategori test data tilhører
    score = model.score(X_test, Y_test)
    print('Test data score: ', score)



def compare_machine_learning_algorithms(filename_machine_learning = 'eksamen'):
    # Get ML data
    all_computers = eksamen_csv.read_csv(filename_machine_learning)
    all_computers_in_list_format = all_computers[1:]
    list_of_machine_learning_sets_numpy_array = create_machine_learning_set_numpy_format(all_computers_in_list_format)

    # Split-out validation dataset
    X = list_of_machine_learning_sets_numpy_array[:, 0:6]
    y = list_of_machine_learning_sets_numpy_array[:, 7]
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)

    # Compare ML algorithms
    support_vector_machines_algorithm(X_train, X_test, Y_train, Y_test)
    decision_tree_classifier_algorithm(X_train, X_test, Y_train, Y_test)
    k_nearestn_eighbors_algorithm(X_train, X_test, Y_train, Y_test)


def machine_learning_with_budget(list_of_machine_learning_sets_numpy_array, computer_to_find_ready_for_machine_learning,
                                 computer_to_find, margin, computer_price, model):
    min_price = float(computer_price) - margin
    max_price = float(computer_price) + margin

    sorted_set = []

    for element in list_of_machine_learning_sets_numpy_array:
        if max_price >= float(element[6]) >= min_price:
            sorted_set.append(element)

    if len(sorted_set) < 5:
        print('\n')
        print(f'There are no computers within the budget of {min_price} kr. to {max_price} kr.')
    else:

        computer_to_find_machine_learning_format = np.array([computer_to_find_ready_for_machine_learning[0:6]])

        # Split-out validation dataset
        sorted_set = np.array(sorted_set)
        X = sorted_set[:, 0:6]
        y = sorted_set[:, 7]
        X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)

        print('\n')
        print('----------')
        print(f'The computer we are looking for with a budget of {min_price} kr. to {max_price} kr.')
        print(computer_to_find)
        print('\n')
        if model == 'CART':
            print('Classification and Regression Trees (CART) result:')
            model = DecisionTreeClassifier()
        elif model == 'SVM':
            print('Support Vector Machines (SVM) result:')
            model = SVC(gamma='auto')
        else:
            print('K-Nearest Neighbors (KNN) result:')
            model = KNeighborsClassifier()

        model.fit(X_train, Y_train)
        print(model.predict(computer_to_find_machine_learning_format))


def machine_learning_with_not_looking_at_budget(list_of_machine_learning_sets_numpy_array,
                                                computer_to_find_ready_for_machine_learning, computer_to_find, model):

    computer_to_find_machine_learning_format = np.array([computer_to_find_ready_for_machine_learning[0:6]])

    # Split-out validation dataset
    X = list_of_machine_learning_sets_numpy_array[:, 0:6]
    y = list_of_machine_learning_sets_numpy_array[:, 7]
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)

    print('\n')
    print('----------')
    print('The computer we are looking for:')
    print(computer_to_find)
    print('\n')
    if model == 'CART':
        print('Classification and Regression Trees (CART) result:')
        model = DecisionTreeClassifier()
    elif model == 'SVM':
        print('Support Vector Machines (SVM) result:')
        model = SVC(gamma='auto')
    else:
        print('K-Nearest Neighbors (KNN) result:')
        model = KNeighborsClassifier()
    model.fit(X_train, Y_train)
    print(model.predict(computer_to_find_machine_learning_format))


def execute_machine_learning(filename_machine_learning = 'eksamen',
                             filename_computer_to_find = 'eksamen_computer_to_find', margin = 0, model = 'CART'):

    # Create the computer we want to find for ML
    computer_to_find_list = eksamen_csv.read_csv(filename_computer_to_find)
    print('\n')
    print(computer_to_find_list)
    computer_to_find = eksamen_class.Computer(computer_to_find_list[0][1], computer_to_find_list[0][6],
                                              computer_to_find_list[0][4], computer_to_find_list[0][5],
                                              computer_to_find_list[0][7], computer_to_find_list[0][9],
                                              computer_to_find_list[0][0], computer_to_find_list[0][2],
                                              computer_to_find_list[0][3])
    #print('\n')
    #print(computer_to_find)
    computer_to_find_ready_for_machine_learning = create_machine_learning(computer_to_find)
    print('\n')
    print(computer_to_find_ready_for_machine_learning)
    print('What we will us:')
    print(computer_to_find_ready_for_machine_learning[0:6])

    # Get ML data
    all_computers = eksamen_csv.read_csv(filename_machine_learning)
    all_computers_in_list_format = all_computers[1:]
    list_of_machine_learning_sets_numpy_array = create_machine_learning_set_numpy_format(all_computers_in_list_format)
    if len(list_of_machine_learning_sets_numpy_array) < 5:
        print('We do not have enough data for Machine Learning....')
    else:
        machine_learning_with_not_looking_at_budget(list_of_machine_learning_sets_numpy_array,
                                                    computer_to_find_ready_for_machine_learning, computer_to_find,
                                                    model)
        machine_learning_with_budget(list_of_machine_learning_sets_numpy_array,
                                     computer_to_find_ready_for_machine_learning, computer_to_find, margin,
                                     computer_to_find.price, model)











