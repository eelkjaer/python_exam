from modules import eksamen_csv
from modules import eksamen_plot
from sklearn.cluster import MeanShift, estimate_bandwidth
import pandas as pd
import numpy as np



def mean_shift_no_quantile(data, n_samples=1000):
    bandwidth = estimate_bandwidth(data, n_samples=n_samples)

    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(data)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters = len(labels_unique)

    print('Number of estimated clusters : {}'.format(n_clusters))

    return labels, cluster_centers, n_clusters


def mean_shift_with_quantile(data, n_samples=1000):
    bandwidth = estimate_bandwidth(data, quantile=0.2, n_samples=n_samples)

    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(data)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters = len(labels_unique)

    print('Number of estimated clusters : {}'.format(n_clusters))

    return labels, cluster_centers, n_clusters


def create_2d_cluster(filename='eksamen', column_1 = 'Price', column_2 = 'Ram', quantile = False):
    csv_data_full = eksamen_csv.return_csv_file_for_head_view(filename)
    cluster_data = csv_data_full[[column_1, column_2]]
    print(cluster_data)
    cluster_data = cluster_data.to_numpy()
    print(cluster_data)

    # change price to int
    if column_1 == 'Price':
        cluster_data_new = []
        for x, y in cluster_data:
            x_token = x.split('.')
            x_number = int(x_token[0])
            # print(x_number)
            cluster_data_new.append([x_number, int(y)])

        cluster_data_new = np.array(cluster_data_new)
        print(cluster_data_new)
    else:
        cluster_data_new = cluster_data

    if quantile:
        labels, cluster_centers, n_clusters = mean_shift_with_quantile(cluster_data_new)
    else:
        labels, cluster_centers, n_clusters = mean_shift_no_quantile(cluster_data_new)

    eksamen_plot.show_clusters(labels, cluster_centers, n_clusters, cluster_data_new)


def create_multi_dimensional_cluster(cluster_data):
    # Find missing values in the data and drop those rows:
    print('rows before drop n/a', len(cluster_data))
    bool_matrix = cluster_data.isnull()  # dataframe with True and False values for each cell in the titanic_data
    only_null_filter = bool_matrix.any(
        axis=1)  # is there a True value in any column in each row. returns a pandas Series with index matching index of titcanic dataframe
    missing = cluster_data[only_null_filter]  # show all rows that has one or more null values
    cluster_data = cluster_data.dropna()
    print('rows after', len(cluster_data))
    cluster_data
    pd.options.display.max_rows = None  # let me see all rows in the dataframe (can be used with columns too)
    bool_matrix

    # what is the best bandwidth to use for our dataset?
    # The smaller values of bandwith result in tall skinny kernels & larger values result in short fat kernels.
    bw = estimate_bandwidth(cluster_data)

    analyzer = MeanShift(bandwidth=bw)
    analyzer.fit(cluster_data)

    labels = analyzer.labels_
    print(labels)
    print('\n\n', np.unique(labels))

    # We will add a new column in dataset which shows the cluster the data of a particular row belongs to.

    # create a new column in the dataset
    cluster_data['cluster_group'] = np.nan
    for i in range(len(cluster_data)):  # loop 714 rows
        cluster_data.iloc[i, cluster_data.columns.get_loc('cluster_group')] = labels[
            i]  # set the cluster label on each row
    print('\n')
    print(cluster_data.head())

    print('\n')
    print(cluster_data.describe())

    # Grouping by Cluster
    df_cluster_data = cluster_data.groupby(['cluster_group']).mean()
    # Count of people in each cluster
    df_cluster_data['Counts'] = pd.Series(cluster_data.groupby(['cluster_group']).size())
    print('\n')
    print(df_cluster_data)




