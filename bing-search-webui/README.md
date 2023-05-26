# Bing Web Search single-page app

This single-page app demonstrates how the Bing Web Search API can be used to retrieve, parse, and display relevant search results based on a user's query. HTML, CSS, and JS files are included. Express.js is the only dependency.

The sample app can:

* Call the Bing Web Search API with search options
* Display web, image, news, and video results
* Paginate results
* Manage subscription keys
* Handle errors

To use this app, an [Azure Cognitive Services account](https://docs.microsoft.com/azure/cognitive-services/cognitive-services-apis-create-account) with Bing Search APIs is required. If you don't have an account, you can visit [the Microsoft Cognitive Services Web site](https://azure.microsoft.com/free/cognitive-services/), create a new Azure account, and try Cognitive Services for free.

## Prerequisites

Here are a few things that you'll to run the app:

* Node.js 8 or later
* A subscription key

## Get started  

1. Clone the repository.
2. Navigate to the Bing Web Search Tutorial directory.
3. Install dependencies:
   ```
   npm install
   ```
4. Run the sample app:
   ```
   node bing-web-search.js
   ```
5. Navigate to the provided URL and perform your first Bing Web Search!

## Next steps

Learn how the app works with the [single-page web app tutorial](https://docs.microsoft.com/en-us/azure/cognitive-services/bing-web-search/tutorial-bing-web-search-single-page-app).

## Screen

![Bing web demo](public\img\screenshot.png "Bing web demo")