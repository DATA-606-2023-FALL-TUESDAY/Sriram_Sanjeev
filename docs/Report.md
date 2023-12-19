# 1. Title and Author

- **Project Title:** YouTube Trending Video Analysis and Predictions
- **Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang
- **Author Name:** Sanjeev Sriram
- **Link to the author's GitHub profile:** [sanjeevsriram3k](https://github.com/sanjeevsriram3k)
- **Link to the author's LinkedIn profile:** [LinkedIn Profile](https://www.linkedin.com/in/sanjeevsriram/)

# 2. Background

## What is it about?

The Trending section of YouTube is designed to highlight videos and clips that a variety of people might find intriguing. Videos on YouTube that have the potential to go viral and gather a lot of viewers are called trending videos. This feature is accessible in many nations worldwide and is updated every day.

## Why does it matter?

It customizes the trending list for each region to showcase videos that are popular in that area.

## What are your research questions?

1. Identify the correlation and significance of various factors that influence a video’s potential for going viral on YouTube.
2. Predict the number of days for which a YouTube video will trend.
3. Predict the view count, likes count, and comment count by the time a video gets out of the trending list.

# 3. Data

## Describe the datasets you are using to answer your research questions.

- **Data sources:** YouTube Trending Video Dataset (updated daily) ([kaggle.com](https://www.kaggle.com/))
- **Data size:** 2 GB
- **Data shape:** 185,990 Rows and 16 Columns
- **Time period:** (Specify if your data is time-bound)

## Data dictionary

- **Columns names:**
  - `video_id` (int): Unique identification for each video.
  - `title` (string): The name of the trending video.
  - `publishedAt` (datetime): Shows the datetime stamp when the video was published.
  - `channelId` (int): Unique identification for each channel on YouTube.
  - `channelTitle` (string): The name of the YouTube channel.
  - `categoryId` (int): An identifier for each category in which a video falls.
  - `trending_date` (datetime): Displays the date and time it appeared on the country’s trending page.
  - `tags` (string): Labels used by channels so YouTube can easily recognize them.
  - `view_count` (int): Number of views on a video.
  - `likes` (int): Number of likes on a video.
  - `dislikes` (int): Number of dislikes on a video.
  - `comment_count` (int): Number of comments on a video.
  - `thumbnail_link` (string): Unique link to every video’s thumbnail image
  - `comments_disabled` (string): Indicates whether comments are disabled.
  - `ratings_disabled` (string): Indicates whether ratings are disabled.

- **Target/Label in ML model:**
  - Multiple target variables (Views, Time, and Days)

- **Variables/Columns as features/predictors for ML models:**
  - categoryID, tags, comment_count etc.

# 4. Exploratory Data Analysis(EDA)

<img src="https://github.com/sanjeevsriram3k/Hello/blob/main/EDA1.jpg">

This displays the NFL leading with the highest number of trending videos among the top 10 YouTube channels.

<img src="https://github.com/sanjeevsriram3k/Hello/blob/main/eda2.png">

this displays Gaming is the category with the most trending videos, significantly ahead of Music and Sports.

<img src="https://github.com/sanjeevsriram3k/Hello/blob/main/eda3.png">

The visualization shows that Music videos have the highest average like-per-view ratio among all categories.

<img src="https://github.com/sanjeevsriram3k/Hello/blob/main/eda4.png">

this is a combination of a box plot and histogram, reveals the distribution of hours it takes for a video to appear on the trending list, with most taking under 10 hours.

<img src="https://github.com/sanjeevsriram3k/Hello/blob/main/eda5.png">

This chart indicates that videos in the Nonprofits & Activism category take the longest average time to trend.

<img src="https://github.com/sanjeevsriram3k/Hello/blob/main/sent1.png">

This image shows a sentiment distribution where the overwhelming majority of videos have positive sentiment.

<img src="https://github.com/sanjeevsriram3k/Hello/blob/main/sent2.png">

this chart highlights that News & Politics has the highest percentage of videos with negative sentiment among different categories.

# 5. Model Training 

### Machine Learning Models Used:

Linear Regression, Decision Tree, and XGBOOST algorithms are employed to predict the comment count on videos.

### Training the Models:

Label encoding is used to convert non-numeric data to numeric data.

MINMAX scaler is applied for normalizing both the features (X) and target (Y) values.

The models are trained on the training data, and their performance is evaluated using the test data.

### Train vs. Test Split:

The dataset is split into 80% for training and 20% for testing purposes.

### Python Packages:

The python packages I used scikit-learn for machine learning models, Pandas for data manipulation, and XGBoost for the XGBOOST algorithm.

### Development Environments:

I used local environment laptop such as Google Colab depending on the availability and the scale of data processing required.

### Measuring and Comparing Performance:

The models are evaluated in terms of Mean Squared Error (MSE) and R2 Score. The MSE should be as low as possible, and the R2 Score should be as close to 1 as possible for the model to be considered accurate.

A comparison graph is also mentioned which plots the algorithms against their MSE and R2 Scores, highlighting that XGBOOST performed the best with the highest R2 Score and the lowest MSE​​.

# 6. Application of the Trained Models

### creating the Web Application:

A web application has been created where users can input video details to predict comment counts.

### Tools for Web App Development:

It appears that the web application is using Django, a high-level Python web framework, which is suitable for developing complex, database-driven websites.

# 7. Conclusion

### Summary

Summarizing your work and its potential application, you have developed predictive analytics models using machine learning algorithms such as Linear Regression, Decision Tree, and XGBOOST to estimate the comment counts on YouTube videos. A web application has been created using Django to allow users to interact with these models, input video details, and receive predictions on comment counts. This application could serve as a valuable tool for content creators and marketers to gauge engagement and strategize their content based on predicted audience interaction.

### Limitations

The limitations of your work may include the reliance on historical data, which may not capture sudden shifts in viewer behavior or trends. The models might also not account for external factors that can influence comment counts, such as viral marketing campaigns or changes in YouTube's recommendation algorithm. Additionally, the web application currently runs on a local server, which may not be scalable for a large number of users.

### Lessons Learned

Lessons learned throughout this process include the intricacies of transforming non-numeric data into a machine-readable format, the importance of data normalization, and the practical application of machine learning algorithms. There's also the realization of the importance of user experience in creating a web interface that allows for easy interaction with complex models.

### Future Research

For future research directions, you could explore the integration of real-time analytics to adjust predictions based on live data. Investigating deeper learning models and natural language processing could provide insights into the sentiment and quality of comments, not just the quantity. Furthermore, deploying the web application in a cloud environment could increase its accessibility and scalability. Exploring advanced security measures to protect user data and ensuring the application's robustness against web vulnerabilities would also be paramount for a publicly accessible tool.


