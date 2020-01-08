import numpy as np
import pandas as pd
import matplotlib as mpl
import seaborn as sns
from matplotlib import pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.cluster import AgglomerativeClustering as AC
from sklearn.metrics import mean_squared_error, r2_score

import matplotlib as mpl

# Changing plot style
plt.style.use('ggplot')

# Setting matplotlib parameters

## Change title size of a plot
mpl.rcParams['axes.titlesize'] = 22
# Figure size
mpl.rc("figure", figsize = (15,7))
## Change label size(x and y) of a plot
mpl.rcParams['axes.labelsize'] = 18
## Change xticks size of a plot
mpl.rcParams['xtick.labelsize'] = 16
## Change yticks size of a plot
mpl.rcParams['ytick.labelsize'] = 16



def barplot(count_series, xlab, ylab, title, color, figure_size = (12, 6), adjust = False):
    plt.figure(figsize = figure_size)
    plt.barh(count_series.index, count_series, color = color, edgecolor = "black")
    plt.ylabel(ylab)
    plt.xlabel(xlab)
    plt.title(title)
    plt.gca().invert_yaxis()
    if adjust:
        for tick in plt.gca().yaxis.get_major_ticks():
            tick.label.set_fontsize(10)
    plt.show()

def lineplot(x, y, xlab, ylab, title, xtickrange, xticklabels = None, 
             color = "blue", marker = "o", x_rotation = 0, figure_size = (14,7)):
    plt.figure(figsize = figure_size)
    plt.plot(x, y, color = color, marker = marker)
    plt.xlabel(xlab)
    if xticklabels:plt.xticks(xtickrange, xticklabels, rotation = x_rotation)
    else: plt.xticks(xtickrange, rotation = x_rotation)
    plt.ylabel(ylab)
    plt.title(title)
    plt.show()

def donut_chart(count_series, title, colors = ["#1F78B4", "#FE7F0E"], explode = (.03, .03), fontsize_pie = 18,
                start_angle = 90, pctdist = 0.80, autopct = '%1.1f%%', circle_rad = 0.60, figure_size = (7, 7)):
    labels = count_series.index
    plt.figure(figsize = (7, 7))
    plt.pie(count_series, colors = colors, autopct = '%1.1f%%', startangle = start_angle, pctdistance = pctdist, 
            explode = explode, labels = labels, textprops = {"fontsize" : fontsize_pie})
    plt.gca().add_artist(plt.Circle((0, 0), circle_rad, fc = 'white'))
    plt.title(title)
    plt.show()


def create_data(df, kind):
    
    if kind == "hour_by_location":
        return df.pivot_table(values='ID', index='Location Description', columns=df.index.hour, 
                                  aggfunc=np.size).fillna(0)
    
    elif kind == "hour_by_type":
        return df.pivot_table(values='ID', index='Primary Type', columns=df.index.hour, 
                                  aggfunc=np.size).fillna(0)
    elif kind == "hour_by_week":
        return df.pivot_table(values='ID', index=df.index.hour, columns=df.index.weekday_name, 
                                           aggfunc=np.size).fillna(0)
    
    elif kind == "dayofweek_by_location": 
        return df.pivot_table(values='ID', index='Location Description', columns=df.index.dayofweek, 
                                  aggfunc=np.size).fillna(0)
    elif kind == "dayofweek_by_type": 
        return df.pivot_table(values='ID', index='Primary Type', columns=df.index.dayofweek, 
                                  aggfunc=np.size).fillna(0)
    else:
        return df.pivot_table(values='ID', index='Location Description', columns='Primary Type', 
                                  aggfunc=np.size).fillna(0)
    
def z_scale(df, axis = "row"):
    if axis == "row":
        return (df - df.mean(axis = 0)) / df.std(axis = 0)
    else:
        return (df - df.mean(axis = 1)) / df.std(axis = 1)

def custom_heatmap(df, shrink, ix = None, cmap='YlOrRd'):
    if ix is None:
        ix = np.arange(df.shape[0])
    sns.heatmap(df.iloc[ix, :], cmap = cmap, square = True, cbar_kws = {"shrink" : shrink}, linewidths = 0.5)
    plt.ylim(0, df.shape[0])
    plt.yticks(np.arange(0, df.shape[0]) + 0.5, df.index[ix])
    plt.xticks(np.arange(0, df.shape[1]) + 0.5)
    plt.grid(False)
    plt.show()


def process_and_plot(df, shrink, ix = None):
    df =  z_scale(df.T).T
    if ix == None:
        ix = AC(4).fit(df).labels_.argsort() # a trick to make better heatmaps
    cap = np.min([np.max(df.values), np.abs(np.min(df.values))])
    df = np.clip(df, -1*cap, cap)
    custom_heatmap(df, shrink, ix = ix)
    
def normalize_df(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

def difference(dataset, interval = 1):
    diff = list()
    for i in range(interval, len(dataset)):
        value = dataset[i] - dataset[i - interval]
        diff.append(value)
    return np.array(diff)

def sequence_plot(data, dates, title, figsize = (15,7), fontsize = 20):
    plt.figure(figsize = figsize)
    plt.plot(dates, data)
    plt.xlabel("Date")
    plt.ylabel("Counts")
    plt.title(title, fontsize = fontsize)
    plt.show()

def fit_ARIMA(data, dates, order, title, disp = 0, trend = "c", residual_plot = False, print_summary = False, figsize = (15,7)):
    series = data
    series.index = pd.to_datetime(dates)
    model = ARIMA(series, order = order)
    model_fit = model.fit(disp = disp, trend = trend)
    if print_summary:print(model_fit.summary())
    if residual_plot:
        residuals = pd.DataFrame(model_fit.resid)
        plt.figure(figsize = figsize)
        residuals.plot()
        plt.title("Residuals plot for " + title)
        plt.legend().set_visible(False)
        plt.show()
    return model_fit.forecast(10)[0]

def plot_true_vs_predicted(true, forecast, dates, title, xpos = 1, ypos = 0.96, fontsize = 16, figsize = (15,7)):
    plt.figure(figsize = figsize)
    rmse = round(np.sqrt(mean_squared_error(true, forecast)), 2)
    r2 = round(r2_score(true, forecast),2)
    plt.plot(dates, true, label = "True", color = "blue", marker = "o")
    plt.plot(dates, forecast, label = "Predicted", color = "red", marker = "o")
    plt.xlabel("Date")
    plt.xticks(rotation = 45)
    plt.ylabel("Count")
    plt.title(title)
    plt.text(xpos, ypos, "RMSE : " + str(rmse), transform = plt.gca().transAxes, fontsize = fontsize)
    plt.text(xpos, ypos - 0.05, "R2 : " + str(r2), transform = plt.gca().transAxes, fontsize = fontsize)
    plt.legend(fontsize = fontsize - 2)
    plt.show()

def plot_ACF_PACF(data, xlags = 100, ylags = 50):
    fig, ax = plt.subplots(1, 2, figsize = (15,7))
    plot_acf(data, lags = xlags, ax = ax[0])
    plot_pacf(data, lags = ylags, ax = ax[1])
    plt.show()

def fit_SARIMA(data, dates, order, sorder, title, trend = "n", residual_plot = False, print_summary = False, figsize = (15,7)):
    series = data
    series.index = pd.to_datetime(dates)
    model = SARIMAX(series, order = order, seasonal_order = sorder, trend = trend)
    model_fit = model.fit()
    if print_summary:print(model_fit.summary())
    if residual_plot:
        residuals = pd.DataFrame(model_fit.resid)
        plt.figure(figsize = figsize)
        residuals.plot()
        plt.title("Residuals plot for " + title)
        plt.legend().set_visible(False)
        plt.show()
    return model_fit.forecast(10)