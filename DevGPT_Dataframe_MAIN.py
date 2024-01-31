import pandas as pd
import json
from langdetect import detect, DetectorFactory, LangDetectException

# nltk.download('vader_lexicon')

# Set seed for the langdetect to get deterministic results
DetectorFactory.seed = 0

# Function to check if the text is in English
def is_english(text):
    try:
        return detect(text) == 'en'
    except LangDetectException:
        return False

# Function to extract relevant information from nested structure
def extract_field(source_list, field_name):
    if isinstance(source_list, list) and len(source_list) > 0:
        return [item.get(field_name, '') for item in source_list if field_name in item]
    return []

# Function to extract 'ChatgptSharing' from nested 'Sources' structure
def extract_chatgpt_sharing(source_list):
    if isinstance(source_list, list) and len(source_list) > 0:
        return [item.get('ChatgptSharing', None) for item in source_list if 'ChatgptSharing' in item]
    return None

# # Function to check if text contains debugging-related keywords
# def contains_debugging_keywords(text, keywords):
#     return any(keyword.lower() in text.lower() for keyword in keywords)

# Function to load JSON data into a DataFrame
def load_json_to_df(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)

    # Check if 'Sources' is a key in the data dictionary
    if 'Sources' in data and isinstance(data['Sources'], list):
        # Normalize each entry in the 'Sources' list into a DataFrame
        # and concatenate them into one DataFrame
        all_dfs = [pd.json_normalize(entry) for entry in data['Sources']]
        combined_df = pd.concat(all_dfs, ignore_index=True)
        return combined_df
    else:
        return None

# # Define debugging keywords
# debugging_keywords = ['error', 'bug', 'fix', 'issue', 'exception', 'crash', 'debug']

# Load the relevant JSON files (replace with actual file paths)
issue_sharings_df = load_json_to_df('D:/DevGPT-main/DevGPT-main/snapshot_20230727/issue_sharings_Copy.json')
commit_sharings_df = load_json_to_df('D:/DevGPT-main/DevGPT-main/snapshot_20230727/commit_sharings_Copy.json')
discussion_sharings_df = load_json_to_df('D:/DevGPT-main/DevGPT-main/snapshot_20230727/discussion_sharings_Copy.json')

########################################### ISSUE #####################################################################
# Printing issue_sharings head
if issue_sharings_df is not None:
    print(issue_sharings_df.head())
else:
    print("Data loading failed.")

# Total rows in issue_sharings
total_rows = issue_sharings_df.shape[0]
print("Total rows:", total_rows)

# Total Duplicate rows in issue_sharings
non_list_columns = issue_sharings_df.select_dtypes(exclude=['object']).columns
duplicate_rows = issue_sharings_df.duplicated(subset=non_list_columns).sum()
print("Total duplicate rows:", duplicate_rows)

# Boolean to check for null values
any_null = issue_sharings_df.isnull().values.any()
print("Are there any null values in the DataFrame?", any_null)

# Printing count of null values in each column
null_values = issue_sharings_df.isnull().sum()
print("Null values in each column:\n", null_values)

# Dropping null values in ClosedAt because that issue is currently active and cannot be analysed
if issue_sharings_df is not None:
    issue_sharings_df = issue_sharings_df.dropna(subset=['ClosedAt'])
    
# Cross checking
any_null = issue_sharings_df.isnull().values.any()
print("Are there any null values in the DataFrame?", any_null)

# Cross checking
null_values = issue_sharings_df.isnull().sum()
print("Null values in each column:\n", null_values)

# Dropping duplicate rows 
issue_sharings_df = issue_sharings_df.drop_duplicates(subset=non_list_columns)

# Cross checking
total_rows = issue_sharings_df.shape[0]
print("Total rows:", total_rows)

# Cross checking
non_list_columns = issue_sharings_df.select_dtypes(exclude=['object']).columns
duplicate_rows = issue_sharings_df.duplicated(subset=non_list_columns).sum()
print("Total duplicate rows:", duplicate_rows)


########################################### COMMIT #####################################################################
# Printing commit_sharings head
if commit_sharings_df is not None:
    print(commit_sharings_df.head())
else:
    print("Data loading failed.")

# Total rows in commit_sharings
total_rows = commit_sharings_df.shape[0]
print("Total rows:", total_rows)

# Checking and printing duplicate rows
non_list_columns = commit_sharings_df.columns[~commit_sharings_df.map(lambda x: isinstance(x, list)).any()]
duplicate_rows = commit_sharings_df.duplicated(subset=non_list_columns).sum()
print("Total duplicate rows in commit_sharings_df:", duplicate_rows)

# Checking null values 
any_null = commit_sharings_df.isnull().values.any()
print("Are there any null values in the DataFrame?", any_null)

# Count of null values in each column 
null_values = commit_sharings_df.isnull().sum()
print("Null values in each column:\n", null_values)

# Dropping duplicate rows
commit_sharings_df_df = commit_sharings_df.drop_duplicates(subset=non_list_columns)

# Cross checking
total_rows = commit_sharings_df.shape[0]
print("Total rows:", total_rows)

# Cross checking
non_list_columns = commit_sharings_df.columns[~commit_sharings_df.map(lambda x: isinstance(x, list)).any()]
duplicate_rows = commit_sharings_df.duplicated(subset=non_list_columns).sum()
print("Total duplicate rows:", duplicate_rows)

################################################################################################################
# Printing discussion_sharings head
if discussion_sharings_df is not None:
    print(discussion_sharings_df.head())
else:
    print("Data loading failed.")

# Total rows in discussion_sharings
total_rows = discussion_sharings_df.shape[0]
print("Total rows:", total_rows)

# Total duplicate rows in discussion_sharings
non_list_columns = discussion_sharings_df.select_dtypes(exclude=['object']).columns
duplicate_rows = discussion_sharings_df.duplicated(subset=non_list_columns).sum()
print("Total duplicate rows:", duplicate_rows)

# Checking for null values
any_null = discussion_sharings_df.isnull().values.any()
print("Are there any null values in the DataFrame?", any_null)

# Printing null values in each column
null_values = discussion_sharings_df.isnull().sum()
print("Null values in each column:\n", null_values)

# Dropping null values from ClosedAt as it is still not resolved 
if discussion_sharings_df is not None:
    discussion_sharings_df = discussion_sharings_df.dropna(subset=['ClosedAt'])

# Cross checking
any_null = discussion_sharings_df.isnull().values.any()
print("Are there any null values in the DataFrame?", any_null)

# Cross checking
null_values = discussion_sharings_df.isnull().sum()
print("Null values in each column:\n", null_values)

# Dropping duplicate rows
discussion_sharings_df = discussion_sharings_df.drop_duplicates(subset=non_list_columns)

# Cross Checking
total_rows = discussion_sharings_df.shape[0]
print("Total rows:", total_rows)

# Cross Checking
non_list_columns = discussion_sharings_df.select_dtypes(exclude=['object']).columns
duplicate_rows = discussion_sharings_df.duplicated(subset=non_list_columns).sum()
print("Total duplicate rows:", duplicate_rows)

###########################################
# Save to CSV
issue_sharings_df.to_csv('issue_sharings_cleaned.csv', index=False)
commit_sharings_df.to_csv('commit_sharings_cleaned.csv', index=False)
discussion_sharings_df.to_csv('discussion_sharings_cleaned.csv', index=False)