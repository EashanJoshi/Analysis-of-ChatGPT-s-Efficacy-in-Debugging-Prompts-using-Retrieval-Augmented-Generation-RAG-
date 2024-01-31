import pandas as pd

# Function to check if text contains debugging-related keywords
def contains_debugging_keywords(text, keywords):
    if isinstance(text, str):
        return any(keyword.lower() in text.lower() for keyword in keywords)
    return False

# Define debugging keywords
debugging_keywords = ['error', 'bug', 'fix', 'issue', 'exception', 'crash', 'debug']

# Load cleaned data from CSV files
issues_df = pd.read_csv('issue_sharings_cleaned.csv')
commits_df = pd.read_csv('commit_sharings_cleaned.csv')
discussions_df = pd.read_csv('discussion_sharings_cleaned.csv')

# Apply keyword-based classification to filter debugging-related entries
issues_df['IsDebuggingRelated'] = issues_df['Body'].apply(lambda x: contains_debugging_keywords(x, debugging_keywords))
commits_df['IsDebuggingRelated'] = commits_df['Message'].apply(lambda x: contains_debugging_keywords(x, debugging_keywords))
discussions_df['IsDebuggingRelated'] = discussions_df['Body'].apply(lambda x: contains_debugging_keywords(x, debugging_keywords))

# Filter for debugging-related entries
debugging_issues = issues_df[issues_df['IsDebuggingRelated']]
debugging_commits = commits_df[commits_df['IsDebuggingRelated']]
debugging_discussions = discussions_df[discussions_df['IsDebuggingRelated']]

# Save the filtered data to new CSV files (optional)
debugging_issues.to_csv('debugging_issues.csv', index=False)
debugging_commits.to_csv('debugging_commits.csv', index=False)
debugging_discussions.to_csv('debugging_discussions.csv', index=False)

# Print the number of debugging-related entries found in each dataset
print("Number of debugging-related issues:", len(debugging_issues))
print("Number of debugging-related commits:", len(debugging_commits))
print("Number of debugging-related discussions:", len(debugging_discussions))
