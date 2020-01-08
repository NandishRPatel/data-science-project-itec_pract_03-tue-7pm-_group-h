
# ITEC657_Practical3_Tuesday_7pm_GroupH 


# Chicago Crime Analysis

Records are being broken and newer peaks are ubiquitous. A great sign, isn’t it? Unfortunately, it is about the crime rates in the glorious city of Chicago. Off late, this region in the United States is on the scanner due to its alarming increase of unlawful, violent acts. Its overall crime rate is significantly higher than the country’s average. The Chicago Police Department’s Bureau of Records has been documenting each felony right from the early 1900s. Just like how technology is getting smarter, the criminals are too. A deeper look into the data will reveal interesting patterns. 


## A. Project Goal

- The main motive of this project is to assess the dataset with a fresh perspective and in a way, answer the following questions:

    **1**. Is there a trend in the crime patterns over the years?
    
    **2**. If there is, what kind of crimes are committed often?
    
    **3**. How does Geography play a role in a potential crime?
    
    **4**. Are there any repeat offenders?
    
    **5**. Has the frequency of incarceration increased/decreased along with the crime rate?
    
    **6**. How have the number arrests corresponded to the crimes changed over time in Chicago?

## B. Data Source and Background

- This dataset echoes reported incidents of horrendous crimes that transpired in the City of Chicago right from 2010 to the current year, 2019. The data is being extracted from the Chicago Police Department's CLEAR (Citizen Law Enforcement Analysis and Reporting) system([Data can be found here!](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2)). It also includes unverified reports and anonymous tips supplied to the Police Department but among a minority. 

- The original dataset (from the year 2001) is in the CSV format comprising 6.96 million observations and 30 features where each row represents a reported crime. A subset (2010-2019) of this huge collection is being considered for further analysis. This subset has around 2.88 million observations with the same number of features.


## C. What can be done with the data?

1. **Data Cleaning** - The data is multi-variate. There are 30 columns among which some require a lot of preprocessing. For example, Columns like ID, Case Number, Year, Updated on, and Location, Historical Wards 2003-2015, Community Areas Wards and many more can be dropped because some of them are not useful and some of them can be derived from the other columns. There are missing values in columns named Location Description, District, Ward, Community Area, Latitude and Longitude, Zip Code and many more. Those records can be dropped as we have a significant amount of observations.

2. **Data Preprocessing** - Integer columns can be converted to ordinal or nominal columns in order to better understand the data. For example - District codes can be replaced with the District name.

3. **Exploratory analysis** – The main aim of doing this is to get familiar with the dataset. Dig through the data and find relationships between variables or to find some trends without any specific goal in mind. For example, Region and crime type.

4. **Explanatory analysis** - Explaining the patterns, relations or trends found while exploring the data.

5. **Data visualization** - Use graphs and plots to explore data, this can be done to answer some basic questions in Exploratory analysis. For example Using Date columns we can see if crimes have changed over years?, Does certain crime happen at certain time of the day, Does holidays has something to do with crimes?, Are some types of crimes more likely to happen in specific locations or specific time of the day or specific day of the week? and many more.


## D. Modelling the data

- Due to the availability of a vast pool of features, there are a plethora of machine learning techniques that can be applied on to data such as:

    **1**. Various kinds of clustering such as hierarchical, K-Means and Time-series clustering, that can be used to group and observe similar characteristic crimes under one roof.
	
	**2**. Classification models such as Random Forest, SVM, Neural networks, etc. to determine the type of the crime based on various features available in the data.
	
	**3**. Factor analysis, Principal component analysis can be done to fetch useful factors/components from a large number of features given in the data.
	
	**4**. Time-series forecasting models like Autoregressive Moving Average (ARMA), Autoregressive Integrated Moving Average (ARIMA), Vector Autoregression Moving-Average (VARMA), Vector Autoregression Moving-Average with Exogenous Regressors (VARMAX) can be applied. (Depending upon a time)

## E. Project Timeline

- Milestones are as following:

    1. [x]  Week 8: All the Data Cleaning and Preprocessing are expected to be done by the end of **Week 8**.
    
    2. [x] Week 9: **Exploratory analysis** is the doorway to see meaningful insights in the data and this is intended to be completed by the end of **Week 9**.
    
    3. [x] Week 10: All the *Modelling techniques* mentioned are set to be completed by the end of **Week 10**.
    
    4. [x] Week 12: Based on all the performance parameters the *best model* will be chosen and interpretation of the insights into a project report will be finished by the end of **week 12**.


## F. Why this dataset?

* You must be wondering why we chose this dataset, as there is so much work done on this dataset. Here's why we want to do this project.

    **1**. Data consists of many features of various types, by choosing this dataset we will be able to learn how to handle mixed data(real-world data, a mixture of numerical, categorical and time-series data). We will also be required to determine which features are useful and which features are just dead-weight.

	**2**. Data consists of a large number of observations(Around 2.88 million), by choosing this dataset we will be able to make models which are scalable.

	**3**. There is so much work done on this dataset - almost every work we found was on time-series analysis and visualization. We haven't found any analysis on the web which is based on forecasting or prediction using complex statistical models mentioned in **D.4**.
