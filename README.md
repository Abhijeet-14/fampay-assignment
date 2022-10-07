# fampay-assignment

# Run Applicaiton

## Problem Statement:

<details>
  <summary>Click to expand!</summary>

### Basic Requirements:

- [ ] Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
- [X] A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- [X] A basic search API to search the stored videos using their title and description.
- [X] It should be scalable and optimized.
- [X] Dockerize the project.

### Bonus Points:

- [X] Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
- [ ] Make a dashboard to view the stored videos with filters and sorting options (optional)

### Instructions:

* You are free to choose any search query, for example: official, cricket, football etc. (choose something that has high frequency of video uploads)
* Try and keep your commit messages clean, and leave comments explaining what you are doing wherever it makes sense.
* Also try and use meaningful variable/function names, and maintain indentation and code style.
* Submission should have a README file containing instructions to run the server and test the API.
* Submission should be done on GitHub Externship Portal.

### Reference:

* [YouTube data v3 API](https://developers.google.com/youtube/v3/getting-started)
* [Search API reference](https://developers.google.com/youtube/v3/docs/search/list)
* To fetch the latest videos you need to specify these: ``type=video, order=date, publishedAfter=<SOME_DATE_TIME>``
  Without publishedAfter, it will give you cached results which will be too old

</details>

## How it Works

* When a client requests data from django, using our REST API, we read the DB for latest data and send back a paginated JSON response.
* I was unable to schedule a background async peroidc task to call YouTube Data API to fetch new videos released after the last hit.
* SO, I created a POST method to do this task.
* The response received is stored in the DB.

## How to Setup:

### Using Docker (Recommended):

```bash
# Clone the repository
  $ git clone https://github.com/Abhijeet-14/fampay-assignment.git

# Checkout to branch master
  $ git checkout docker-branch

# create .env value inside fampay_assignment (Not in root)
	# copy .env values from mail.
# Build Image
 $ docker build -t fampay_assign:latest -t fampay_assign:v1 .

# Run Continaer
 $ docker run --name fampay_assign_container -d -p 8000:8000 fampay_assign:latest  

# The server should be up on port 8000, API usage same as shown below 
```

* Add data to DB "http://localhost:8000/v1/api/youtubevideos/" "POST" in your browser to see the API response.
* Visit "http://localhost:8000/v1/api/youtubevideos/?limit=10&offset=5" "GET" in your browser to see the API response.
* search by titlte or description "http://localhost:8000/v1/api/search/?title=tea&description=good" "GET" in your browser to see the API response.
