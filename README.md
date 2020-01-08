## Group: ITEC657_Practical3_Tuesday_7pm_GroupH

## Group Members: 

 - Nandish Patel([nandishpatel1996](https://github.com/nandishpatel1996))
 - Tarun kumar([tarun1195](https://github.com/tarun1195))
 - Sai Kiran Ravula([venkatasaikiranravula](https://github.com/venkatasaikiranravula))
 - Ali Saeed([Ali0Saeed](https://github.com/Ali0Saeed))

## Project Title: Chicago Crime Analysis

## Introduction:
In this project we are analyzing the different aspects of high crime rate that happen in Chicago to find out the possible patterns so as to reduce them in future. The aspects include the following:
        1) Different types of crimes.
        2) The impact of geography.
        3) The number of arrests that happen. 
The number of crimes happening in different district are analyzed to determine where the crime are happening the most and where the least. Different type of crimes like theft, battery and robbery are also compared to find the most common type of crimes in the city. Finally the number of arrests that happen over a last decade(2010-2019) are also inspected to compare the crime rate against the number of arrests. 
       
## Dataset: 
The dataset comprises a number of trivial and horrifying crimes that happen in the city of Chicago from 2010 to 2019. The dataset is accumulated from Chicago Police Department's CLEAR (Citizen Law Enforcement Analysis and Reporting) system. It encompasses some unverified report and tips to the police as well.The dataset contains 30 distinct features and over 6.9 million different records originally. Each record represents a different crime. A significant part of the original dataset comprising over 2.8 million records is utilized in this analysis.

## Data Preprocessing:
 As the dataset contains a large number of records, it must have some unnecessary and missing data due to which the performace could be impacted adversly. All the records that have missing values are removed and some columns like FBI Code and X Coordinate are dropped as they were not very important. To better use the variables, the data type of some varialbes is changed. 
                    
## Methodology:
After the preprocessing, the the dataset is splitted into train, test and validation sets. After that the classifer is trained on training set and then evaluated on test and validation sets.
To deteremine the possible crime patterns, a number of machine learning classifiers are applied. Some of the classifers include:
1) Logistic regression.
2)RandomForest
3)GaussianNB
4)MLPClassifier
5)Naive Baye's
6)Neural Network
In addition to that various python plotting libraries like 'seaborn', 'pyplot' and 'matplot' are utilized to determine pattterns, make comparisons and finding the impact of different aspects of crimes.

## Result & Analysis: 
Some very important and unexplored patterns and specifics that are determined are as follows:
  Over the period of last ten years, the  crimes have deceased significantly.
  The crimes occur in large numbers  in the month of July & August.
  The theft &  Battery type crimes have occurred the most & the Robbery  type the least.
  The crimes have occurred  the most in Streets & Residential areas & the least  in Restaurants.
  Only a quarter of criminals are arrested.
  Over a last decade, the number of criminals arrested have decreased.
  There is a significant decrease in the number of domestic crimes.
  Overall the rate of crimes and arrests have declined.









