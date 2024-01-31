import warnings
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

# Suppress specific warnings related to timezone information in Period conversion
warnings.filterwarnings("ignore", message="Converting to PeriodArray/Index representation will drop timezone information.")

# Load the data
issues_df = pd.read_csv('debugging_issues.csv')
commits_df = pd.read_csv('debugging_commits.csv')
discussions_df = pd.read_csv('debugging_discussions.csv')

# Convert date columns to datetime
issues_df['CreatedAt'] = pd.to_datetime(issues_df['CreatedAt'], utc=True)
issues_df['ClosedAt'] = pd.to_datetime(issues_df['ClosedAt'], utc=True)
discussions_df['CreatedAt'] = pd.to_datetime(discussions_df['CreatedAt'], utc=True)
discussions_df['ClosedAt'] = pd.to_datetime(discussions_df['ClosedAt'], utc=True)
commits_df['AuthorAt'] = pd.to_datetime(commits_df['AuthorAt'], utc=True)
commits_df['CommitAt'] = pd.to_datetime(commits_df['CommitAt'], utc=True)


def extract_year_month(datetime_series):
    return datetime_series.dt.to_period('M')

# Apply the function to each DataFrame
issues_df['YearMonth'] = extract_year_month(issues_df['CreatedAt'])
commits_df['YearMonth'] = extract_year_month(commits_df['AuthorAt'])
discussions_df['YearMonth'] = extract_year_month(discussions_df['CreatedAt'])

# Count the number of issues, commits, and discussions per month
issues_trend = issues_df.groupby('YearMonth').size()
commits_trend = commits_df.groupby('YearMonth').size()
discussions_trend = discussions_df.groupby('YearMonth').size()

# Combine the trends into a single DataFrame
combined_trend = pd.concat([issues_trend, commits_trend, discussions_trend], axis=1)
combined_trend.columns = ['Issues', 'Commits', 'Discussions']

# Print the combined trend data
print(combined_trend)

# Define a function to count ChatGPT mentions
def count_chatgpt_mentions(df, column_name):
    return df[column_name].apply(lambda x: len(x) if x is not None else 0).sum()

# Count ChatGPT mentions in each dataset
issues_chatgpt_mentions = count_chatgpt_mentions(issues_df, 'ChatgptSharing')
commits_chatgpt_mentions = count_chatgpt_mentions(commits_df, 'ChatgptSharing')
discussions_chatgpt_mentions = count_chatgpt_mentions(discussions_df, 'ChatgptSharing')

# Print ChatGPT mention counts
print("ChatGPT Mentions in Issues:", issues_chatgpt_mentions)
print("ChatGPT Mentions in Commits:", commits_chatgpt_mentions)
print("ChatGPT Mentions in Discussions:", discussions_chatgpt_mentions)

# Analyze the resolution time for issues
issues_df['ResolutionTime'] = issues_df['ClosedAt'] - issues_df['CreatedAt']
avg_resolution_time = issues_df['ResolutionTime'].mean()
avg_resolution_time_by_language = issues_df.groupby('RepoLanguage')['ResolutionTime'].mean()

# Sentiment Analysis Setup
sia = SentimentIntensityAnalyzer()
issues_df['Sentiment'] = issues_df['Body'].apply(lambda x: sia.polarity_scores(x)['compound'] if isinstance(x, str) else 0)
avg_sentiment = issues_df['Sentiment'].mean()

# Analyze the correlation between ChatGPT mentions and upvote counts in discussions
discussions_df['ChatgptMentionsCount'] = discussions_df['ChatgptSharing'].apply(lambda x: len(x) if x is not None else 0)
correlation = discussions_df[['ChatgptMentionsCount', 'UpvoteCount']].corr().iloc[0, 1]

# Calculate correlation between ResolutionTime and programming languages
issues_df['LanguageNumeric'] = issues_df['RepoLanguage'].astype('category').cat.codes
correlation_1 = issues_df[['LanguageNumeric', 'ResolutionTime']].corr().iloc[0, 1]

# Print analysis results
print("Average Issue Resolution Time:", avg_resolution_time)
print("Average Issue Resolution Time for each language:", avg_resolution_time_by_language)
print("Average Sentiment of Issue Bodies:", avg_sentiment)
print("Correlation between ChatGPT Mentions and Upvotes in Discussions:", correlation)
print("Correlation between Resolution Time and Programming Languages:", correlation_1)

# Additional analysis and visualizations can be added here
