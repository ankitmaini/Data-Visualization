Introduction
A web API is a part of a website designed to interact with programs that use very specific URLs to request certain information. This kind of request is called an ### API call.
The requested data will be returned in an easily processed format such as JSON or CSV. Most apps that rely on external data sources such as apps that integrate with social media sites, rely on API calls.


### Git and GitHub
I will be using the GitHub's API to request information about python projects on the site and then generate an interactive visualization of the relative popularity of these projects in Pygal.

# Aim:
To write a program to automatically download information about the most-starred Python Projects on GitHub and then create an informative visualization of these projects.

# Requesting Data using an API call
https://api.github.com/search/reositories?q=language:pythono&sort=stars
