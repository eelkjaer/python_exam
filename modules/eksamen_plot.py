import matplotlib.pyplot as plt
import numpy as np
from itertools import cycle


def plot_result(total_result):
    x = []
    y = []
    count = 1

    for result in total_result:
        x.append(str(count) + ': ' + str(result['title'][6:25]))
        y.append(result['price'])
        # print(x)
        # print(y)
        count = count + 1

    plt.figure(figsize=(12, 12))

    plt.bar(x, y, width=0.4, linewidth=0, align='center', color='blue', alpha=0.9, label="Price")


    plt.title('Scrape Result', fontsize=16)
    # plt.xlabel('Macbook')
    plt.ylabel('Price DDK', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.xticks(rotation=45, horizontalalignment='right', fontweight='light')
    plt.legend()
    plt.show()


def plot_price_ram(csv_data):
    plt.figure(figsize=(12, 12))
    plt.plot(csv_data['Price'].astype(float), csv_data['Ram'].astype(float), 'b.')
    plt.plot([10000, 42500], [8, 64], label='quantiles')
    plt.plot([10000, 45000], [8, 45], label='non quantiles')

    # x = np.array([15000, 22500, 36300, 42500])
    # y = np.array([8, 16, 32, 64])
    # plt.plot(x, y, label='ex-curv 1')

    # x = np.array([15000, 22500, 34000, 44500])
    # y = np.array([8, 16, 32, 64])
    # plt.plot(x, y, label='ex-curv 1')

    plt.title('Ram / Price')
    plt.xlabel('Price DDK')
    plt.ylabel('Ram size')
    plt.legend()


def plot_price_ram_normalize(csv_data):
    plt.figure(figsize=(12, 12))
    plt.plot(csv_data['Price'].astype(float), csv_data['Ram'].astype(float), 'b.')
    plt.plot([0, 0.9], [0, 1], label='quantiles')
    plt.plot([0, 1], [0, 0.7], label='non quantiles')

    # x = np.array([0, 0.55, 0.9])
    # y = np.array([0, 0.41, 1])
    # plt.plot(x, y, label='ex-curv 1')

    # x = np.array([15000, 22500, 34000, 44500])
    # y = np.array([8, 16, 32, 64])
    # plt.plot(x, y, label='ex-curv 1')

    plt.title('Ram / Price')
    plt.xlabel('Price DDK')
    plt.ylabel('Ram size')
    plt.legend()


def plot_price_screen(csv_data):
    plt.figure(figsize=(12, 12))
    plt.plot(csv_data['Price'].astype(float), csv_data['Screen'].astype(int), 'b.')
    plt.plot([12500, 35000], [13, 16], label='quantiles')
    plt.plot([12500, 42000], [13, 16], label='non quantiles')

    #x = np.array([12500, 25000, 38000])
    #y = np.array([13, 14, 16])
    #plt.plot(x, y, label='ex-curv 1')

    # x = np.array([15000, 22500, 34000, 44500])
    # y = np.array([8, 16, 32, 64])
    # plt.plot(x, y, label='ex-curv 1')

    plt.title('Screen / Price')
    plt.xlabel('Price DDK')
    plt.ylabel('Screen size')
    plt.legend()


def show_clusters(labels, cluster_centers, n_clusters, cluster_data):
    # Plot the clusters in different colors
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111)

    colors = cycle('bgrcmy')
    for k, col in zip(range(n_clusters), colors):
        my_members = (labels == k)
        # print(my_members)
        cluster_center = cluster_centers[k]
        print(cluster_center)

        x, y = cluster_data[my_members, 0], cluster_data[my_members, 1]
        # print(x)
        # print(y)
        ax.scatter(x, y, c=col, linewidth=0.2)
        ax.scatter(cluster_center[0], cluster_center[1], c='k', s=50, linewidth=0.2)

    plt.title('Estimated number of clusters: {}'.format(n_clusters))


