# Data_Science_Final_Project

## Introduction

The objective of this project is to use Jupyter and its imports to analyze Uber Data. I wanted to know when the best time to take an uber would be, that being the time with the lowest amount of rides. I quickly realized that a lot of people take ubers and the amount of data that would be in a avaliable for a given year across the USA would be too much for my small computer to handle. So I bagan searching Kaggle.

On Kaggle I was able to find a "small" data set from 2014 in NY. [here](https://github.com/buteaunatwit/Data_Science_Final_Project/blob/main/Final_Noah_Buteau_Uber_Data_Analysis.ipynb). I will use this to answer a my questions:

When is the most travled time during the day?
Week?
When is the least travled time during the day?
Week?

## Selection of Data
What is the source of the dataset?

The source of the dataset comes from [here](https://www.kaggle.com/datasets/fivethirtyeight/uber-pickups-in-new-york-city), a post from kaggle that does have more months included but I chose to focus of the July 2014 data.

Characteristics of data?

The model processing and training are conducted using a Jupyter Notebook and is available [here](https://github.com/memoatwit/dsexample/blob/master/Insurance%20-%20Model%20Training%20Notebook.ipynb).

The table consitst of 796121 rows and 8 columns.
The objective is find the best time and day to take an uber.
The column names are Date/Time,	Lat, Lon,	Base. Date/Time being the date and time, Lat being the latitude, Lon being the longitude, Base the The TLC base company code affiliated with the Uber pickup.

Any munging, imputation, or feature engineering?
For my question I did not need Lat and Lon so I decided to drop those columns. Shown here:

![Image#0](https://user-images.githubusercontent.com/77858100/206063527-55884e58-66de-471c-9d85-08f60a2ad0d4.JPG)

To make the date and time more readable I converting them from a str value to a datetime value and then to data/time more usable I split them into their own respective columns. Those columns being timeOfDay, dayOfWeek, and date. Before making them all their own columns I floored the times to the 15 minute mark to make the data easier to analyze in a graph. Those changes are shown below:

![Image6](https://user-images.githubusercontent.com/77858100/206064711-cc9bf203-d5e2-4cff-80c4-b0489c14771c.JPG)
![day](https://user-images.githubusercontent.com/77858100/206065259-a166ee56-ea40-4027-8566-b83cbdcd86cc.JPG)
![date](https://user-images.githubusercontent.com/77858100/206065268-c080e8a4-702c-4ccc-82d5-9a5051ddcec0.JPG)
![timeOfDay](https://user-images.githubusercontent.com/77858100/206065279-31b55283-1503-44a7-b6f1-96448e2b284d.JPG)
![floor](https://user-images.githubusercontent.com/77858100/206065395-52080acf-0e19-42a3-b3dd-be0e54c1dab8.JPG)

## Methods

Tools:
- NumPy, Pandas, matplotlib.pyplot, and seaborn
- Juypter for coding 

These tools were used to graph and to anaylze the data.

## Results
My results are shown below in the following graphs:

![Image#1](https://user-images.githubusercontent.com/77858100/206062544-f28c63f3-93c6-48ca-8c48-a2a7d411db8b.JPG)
![Image#2](https://user-images.githubusercontent.com/77858100/206062617-6827794e-0525-4860-9db4-7c33df377a5d.JPG)

(The first graph is in bar plot and the second is in line plot)

In this graph we are shown the amount of rides over the course of the month. The interesting thing about this is the trend that repeats itself every seven days. This being the weekly cycle. This doesnt really answer our question and seems to be too inconclusive and too inconsitant to definetly say what day we should travel on. So lets go another step and look into the average rides per week in  the month of July.

![Image#3](https://user-images.githubusercontent.com/77858100/206062639-a7949f4a-126b-4b49-b1d8-9a53f5eba5a1.JPG)

Our second graph here shows the average amount of rides taken per each day of the week. This allows us to narrow down the day upon which the least amount of rides occur. That day being Monday. Now we know which day to travel but now we want to figure out which time of the day would be the best to travel at. Not only for monday !
but for all the days as well.

![Image#4](https://user-images.githubusercontent.com/77858100/206062697-129e712e-e378-4b7e-8b1d-af55412ab568.JPG)

The image of above shows a heatmap of the average amount of rides at specific times during each day of the week. This allows us to pinpoint the busiest days and times during the week. This time being around 5:30 pm - 6:15 pm. The day and time being the least busy is from 12 am - 3 am on the days Monday-Thursday. 

![Image#5](https://user-images.githubusercontent.com/77858100/206062703-ba6e0503-e860-4039-9f8c-9a5b9246df7b.JPG)

The last images what the heatmap showed but in a line plot for easier repersentation.

ANSWER:
When is the most travled time during the day?

- 5:30-6:15 pm

When is the most travled time during the week?

- Tuesday

When is the least travled time during the day?

- 12:00 - 3:00 am

When is the least travled time during the week?

- Monday

## Discussion

For my dataset we are in the time period of July 2014 in NYC a commonly travled place by most. With this dataset we are able to predict the buisest times during the days of the weeks in the month of July. The answers to the question help people who are traveling to NYC in the following year. Those indivduals can use this data to predict when the hardest times to get an uber will be. They can also see when the highest average amount of rides occur allowing them to plan their night effiectivly. For instance if you wanted to spend your night in time square till 1:00 am the amount of rides that occur at that time are close to none so you may have isssues getting a ride. 

Issues with this data are as follows; The amount of uber drivers avaliable at these times are not shown, what if your traveling in a different month, the cost is not shown, etc. We are not able to see if the amount of rides correlates to the amount of drivers or the amount of people on the app the request a ride. This would proove useful beacuse at the moment while 1:00 am seems to the the least travled time, so does this mean you should take an uber so that you are guaranteed a ride or should you not request an uber because no one is providing a service. The dataset only tracks the month of July so if you are planning to travel a different month you can use the same methodologies used on this dataset but could not come to a conclusion for those months bashed on this one. Another factor when determining a ride time is the price. The price was not giving for each ride so our answer is soley based on the amount of riders.

The analysis on the dataset above is useful because shows us the times to avoid during the week and during the day when traveling to NYC. This would be most acurate if your traveling a year after this data set is released but because less and less acurate as the years go on.

This project could be imporved over time by simply adding data from the years to come to keep the estimates accurate.

## Summary



## References
[1] [GitHub Integration (Heroku GitHub Deploys)](https://devcenter.heroku.com/articles/github-integration)

[2] [Streamlit](https://www.streamlit.io/)

[3] [The pycaret post](https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104)

[4] [Insurance dataset: git](https://github.com/stedy/Machine-Learning-with-R-datasets)

[5] [Insurance dataset: kaggle](https://www.kaggle.com/mirichoi0218/insurance)
