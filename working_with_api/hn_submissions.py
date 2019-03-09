import requests

from operator import itemgetter

# Make an API call and store the response. A call is made here to the API and the API call returns a list containing the IDs of the 500 most popular articles on Hacker News at the time the call is issued.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status code:', r.status_code)

# Process information about each submission. Here the response text is converted to a Python list which is stored in submission_ids. We will use these IDs to build a set of dictionaries that each store information about one of the current submissions.
submission_ids = r.json()

# A dictionary is set up to store these dictionaries.
submission_dicts = []

# Looping through the IDs of the top 30 submissions. 
for submission_id in submission_ids[:30]:
    
    # Make a separate API call for each submission by generating a URL that includes the current value of submission_id added to the basic redirection URL.
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')

    # A request is made to the combined URL each time
    submission_r = requests.get(url)

    # We print the status of each request to see whether it was successful or not and read it.
    print(submission_r.status_code)
    response_dict = submission_r.json()

    # We create a dictionary for the submission currently being processed, where we store the title of the submission and a link to the discussion page for that item.
    submission_dict = {
        'title' : response_dict['title'],
        'link' : 'http://news.ycombinator.com/item?id=' + str(submission_id),
        
        # Here we store the number of comments in the dictionary. In case there are no comments present, the key 'descendants' will be absent. Thus, when we are not sure if a key is present in a dictionary, we can use the dict.get(a = key, b = response if key not present).
        'comments' : response_dict.get('descendants', 0)
    }
    # Appending the submission_dict to a combined dictinary: submission_dicts
    submission_dicts.append(submission_dict)

# Sorting the sub-dictionaries of this main dictionary according to the number of comments.
submission_dicts = sorted(submission_dicts, key = itemgetter('comments'), reverse = True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])
