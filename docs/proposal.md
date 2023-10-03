# 1. Title and Author

- **Project Title:** YouTube Trending Video Analysis and Predictions
- **Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang
- **Author Name:** Sanjeev Sriram
- **Link to the author's GitHub profile:** [sanjeevsriram3k](https://github.com/sanjeevsriram3k)
- **Link to the author's LinkedIn profile:** [LinkedIn Profile](#)

# 2. Background

## What is it about?

The Trending section of YouTube is designed to highlight videos and clips that a variety of people might find intriguing. Videos on YouTube that have the potential to go viral and gather a lot of viewers are called trending videos. This feature is accessible in many nations worldwide and is updated every 15 minutes.

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
  - (Specify relevant columns)
