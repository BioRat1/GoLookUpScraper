# GoLookUpScraper
A little GoLookUp scraper I made for Kanary

I loved this challange, especially since it was a refresher on my knowledge of Requests and BeautifulSoup. GoLookUp doesn't have a public API which made me
have to use "Inspect Element" to find an endpoint to send a post request to, the payload containing the first and last name. The endpoint needed to be where the post request is sent to get the results back and that endpoint was "https://golookup.com/lander/people/default/processPeopleSearch"

I then had to find the endpoint where the results came back to send a get request and that was "https://golookup.com/lander/people/default/results"

GoLookUp was blocking me from scraping so I had to use a differant header which is where the "header=header" came into play

Once I had the "post" and the "get" request situated, that was all I needed. I then used BeautifulSoup to filter and  structure the data.

Thank you Kanary  so much for giving me this oppertunity to brush up on these skills
