# Day 45: Movie Scraper using Beautiful Soup

## Description
This Python script scrapes a webpage containing a list of movies and saves the movie titles to a text file (`movies.txt`). The movies are listed in reverse order of appearance on the webpage.

## How it Works
1. The script sends an HTTP GET request to the website URL using the `requests` library.
2. It then parses the HTML content of the webpage using `BeautifulSoup`.
3. The movie titles are extracted from the HTML elements where they are stored.
4. The titles are reversed and written to a text file named `movies.txt`.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4
```

## How to Run the Project
1. Clone the repository or download the Python script.
2. Make sure you have installed the necessary libraries.
3. Run the Python script using the following command:
```bash
python <onehundred_movies_to_watch>.py
```
4. The movie titles will be written to `movies.txt`.

## About Beautiful Soup
`BeautifulSoup` is a Python library used for parsing HTML and XML documents. It allows you to extract specific elements, search by tag names or CSS classes, and navigate through the tree structure of a webpage's HTML.

In this script, BeautifulSoup is used to:
- Parse the raw HTML content of the webpage.
- Find all the `<h3>` tags with a specific class containing movie titles.
- Extract and process those titles for further use.

`BeautifulSoup` makes web scraping easier by offering an easy-to-use API for searching and modifying the document tree.
