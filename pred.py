import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

dates = []
prices = []


def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            # assume date string like '2013-01-02' and price in second column
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))


def predict_prices(dates, prices, x):
    dates = np.reshape(dates, (len(dates), 1))

    svr_lin = SVR(kernel='linear', C=1e3)
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)

    print('starting fit')
    svr_lin.fit(dates, prices)
    print('lin done')
    svr_rbf.fit(dates, prices)
    print('rbf done')

    plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
    plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()

    # ensure x has shape (n, 1)
    if isinstance(x, (int, float)):
        x = np.array([[x]])
    else:
        x = np.reshape(x, (len(x), 1))

    preds = (svr_rbf.predict(x)[0], svr_lin.predict(x)[0])
    print('preds computed:', preds)
    return preds


if __name__ == '__main__':
    # update filename as needed; expects a file named aapl.csv in the same folder
    get_data('aapl.csv')
    print('loaded rows:', len(dates))
    print('dates:', dates)
    print('prices:', prices)
    predicted_price = predict_prices(dates, prices, 29)
    print('predicted_price:', predicted_price)