# news

## Author

[Brian Otieno](https://github.com/default-007)

## Description

This is an application that will help people who want to get realtime news withouth having to watch TV for the news. The website will show news articles from several sources and news sources that a user can click to see morw news. The application consumes news from the [News API](https://newsapi.org/)

## Live Demo

Click [Link](https://news-007.herokuapp.com/) to visit the site

## BDD

| Behavior                               | Input | Output                                                                                        |
| -------------------------------------- | ----- | --------------------------------------------------------------------------------------------- |
| Display Various news from news sources | None  | Display the top news articles from various news sources like CNN, FOX NEWS, ESPN, NBC and ABC |

## Development Installation

To get the code..

1. Cloning the repository:

```bash
git clone https://github.com/default-007/news.git
```

2. Move to the folder and install requirements

```bash
cd news
pip install -r requirements.txt
```

3. Exporting Configurations

```bash
export API_KEY='{Enter your News Api Key}'
```

4. Running the application

```bash
python3.8 manage.py server
```

5. Testing the application

```bash
python3.8 manage.py test
```

Open the application on your browser `127.0.0.1:5000`.

## Technology used

- [Python3.8](https://www.python.org/)
- [Flask](http://flask.pocoo.org/)
- [Heroku](https://heroku.com)

## Known Bugs

- There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information

If you have any question or contributions, please email me at [brianokola@gmail.com]

## License

- _MIT License:_
- Copyright (c) 2019 **Brian Otieno**
