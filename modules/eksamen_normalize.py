from modules import eksamen_csv
import sklearn
# import sklearn.linear_model
# from sklearn import preprocessing
import seaborn as sb
import pandas as pd


def pairplot_and_normalization(filename='eksamen', mode = 'all', quantile = False):
    csv_data_full = eksamen_csv.return_csv_file_for_head_view(filename)

    csv_data_sorted = csv_data_full[["Processor", "Ram", "SSD (TB)", "Screen", "Price"]]

    print(csv_data_sorted.head())

    # Convert processor to 0, 1 or 2
    label_enc = sklearn.preprocessing.LabelEncoder()
    csv_data_sorted['Processor'] = label_enc.fit_transform(csv_data_sorted['Processor'].astype(str))

    print('\n')
    print(csv_data_sorted)

    # Normalization data
    scaler = sklearn.preprocessing.MinMaxScaler()
    names = csv_data_sorted.columns
    d = scaler.fit_transform(csv_data_sorted)
    scaled_df = pd.DataFrame(d, columns=names)

    print(scaled_df[10:31])

    if mode == 'all':
        sb.pairplot(scaled_df)
    elif mode == 'screen_price':
        screen_price_scaled = scaled_df[['Screen', 'Price']]
        print('\n')
        print(screen_price_scaled.head())
        sb.pairplot(screen_price_scaled)

        if quantile:
            print('\n')
            print('With quantile 10 -> 90')
            dataSet_minus_upper_procent = (
            screen_price_scaled.loc[screen_price_scaled['Price'].astype(float) < screen_price_scaled['Price'].astype(float).quantile(0.90)])
            dataSet_minus_bottom_procent = (dataSet_minus_upper_procent.loc[
                dataSet_minus_upper_procent['Price'].astype(float) > dataSet_minus_upper_procent['Price'].astype(
                    float).quantile(0.10)])
            print(dataSet_minus_bottom_procent)
            sb.pairplot(dataSet_minus_bottom_procent)

    elif mode == 'ram_price':
        ram_price_scaled = scaled_df[['Ram', 'Price']]
        print('\n')
        print(ram_price_scaled.head())
        sb.pairplot(ram_price_scaled)

        if quantile:
            print('\n')
            print('With quantile 10 -> 90')
            dataSet_minus_upper_procent = (
            ram_price_scaled.loc[ram_price_scaled['Price'].astype(float) < ram_price_scaled['Price'].astype(float).quantile(0.90)])
            dataSet_minus_bottom_procent = (dataSet_minus_upper_procent.loc[
                dataSet_minus_upper_procent['Price'].astype(float) > dataSet_minus_upper_procent['Price'].astype(
                    float).quantile(0.10)])
            print(dataSet_minus_bottom_procent)
            sb.pairplot(dataSet_minus_bottom_procent)


def create_dummies(cluster_data, column):
    # One-hot encoding of 'Embarked' with pd.get_dummies
    cluster_data = pd.get_dummies(cluster_data, columns=[column])
    print(cluster_data.head())
    return cluster_data


def normalize_csv_data(csv_data):
    scaler = sklearn.preprocessing.MinMaxScaler()
    names = csv_data.columns
    d = scaler.fit_transform(csv_data)
    scaled_df = pd.DataFrame(d, columns=names)
    return scaled_df





