from modules import eksamen_csv
import sklearn.linear_model
import numpy as np


def create_linear_regression(filename = 'eksamen', column_1 = 'Price', column_2 = 'Ram'):
    csv_data = eksamen_csv.return_csv_file_for_head_view(filename)
    print(csv_data)

    xs = csv_data[column_1].astype(float)
    ys = csv_data[column_2].astype(float)

    #print('\n')
    #print('X is:')
    #print(xs)

    #print('\n')
    #print('Y is:')
    #print(ys)

    xs_reshape = np.array(xs).reshape(-1, 1)
    #print('\n')
    #print(xs.shape)
    #print(xs_reshape.shape)
    #print(xs_reshape)

    model = sklearn.linear_model.LinearRegression()
    model.fit(xs_reshape, ys)

    model.coef_
    print('\n')
    print('For hver 1 kr. stiger {} med {}'.format(column_2, model.coef_))

    # model.intercept_
    # print('\n')
    # print('The intercept (often labeled the constant) is the expected mean value of Y when all X=0 - {}'.format(model.intercept_))

    predicted = model.predict(xs_reshape)
    spending10000 = model.predict([[10000]])
    print('\n')
    print('Spending 10000 kr on MacBook means {} will be the {} size'.format(spending10000[0], column_2))
    predicted

    predicted = model.predict(xs_reshape)
    spending20000 = model.predict([[20000]])
    print('\n')
    print('Spending 20000 kr on MacBook means {} will be the {} size'.format(spending20000[0], column_2))
    predicted

    predicted = model.predict(xs_reshape)
    spending30000 = model.predict([[30000]])
    print('\n')
    print('Spending 30000 kr on MacBook means {} will be the {} size'.format(spending30000[0], column_2))
    predicted

    predicted = model.predict(xs_reshape)
    spending40000 = model.predict([[40000]])
    print('\n')
    print('Spending 40000 kr on MacBook means {} will be the {} size'.format(spending40000[0], column_2))
    predicted


