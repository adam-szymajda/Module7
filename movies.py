import datetime

class Movie():
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.playbacks = 0

    def __str__(self):
        return f'{self.title} ({self.year})'

    def play(self, value=1):
        self.playbacks += value

class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f'{self.title} S{self.season:0>2d}E{self.episode:0>2d}'

def get_series():
    series = [title for title in titles if isinstance(title, Series)]
    return sorted(series, key=lambda x: x.title, reverse=True)

def get_movies():
    movies = [title for title in titles if not isinstance(title, Series)]
    return sorted(movies, key=lambda x: x.title, reverse=True)

def search(phrase):
    temp = [title for title in titles if phrase.lower() in title.title.lower()]
    for title in temp:
        print(title)


returnofthejedi = Movie(title='Return of the Jedi', year=1979, genre='Science Fiction')
fellowshipofthering = Movie(title='Fellowship of the Ring', year=2002, genre='Fantasy')
twotowers = Movie(title='The Two Towers', year=2003, genre='Fantasy')
returnoftheking = Movie(title='Return of the King', year=2004, genre='Fantasy')
drhouse_s01e01 = Series(title='Dr House', year=2010, genre='drama', season=1, episode=1)
drhouse_s01e02 = Series(title='Dr House', year=2010, genre='drama', season=1, episode=2)
drhouse_s01e03 = Series(title='Dr House', year=2010, genre='drama', season=1, episode=3)
drhouse_s01e04 = Series(title='Dr House', year=2010, genre='drama', season=1, episode=4)
drhouse_s01e05 = Series(title='Dr House', year=2010, genre='drama', season=1, episode=5)
drhouse_s01e06 = Series(title='Dr House', year=2010, genre='drama', season=1, episode=6)
drhouse_s01e07 = Series(title='Dr House', year=2010, genre='drama', season=1, episode=7)
thewitcher_s01e01 = Series(title='The Witcher', year=2019, genre='fantasy', season=1, episode=1)
thewitcher_s01e02 = Series(title='The Witcher', year=2019, genre='fantasy', season=1, episode=2)
thewitcher_s01e03 = Series(title='The Witcher', year=2019, genre='fantasy', season=1, episode=3)


titles = [returnofthejedi, drhouse_s01e01, drhouse_s01e02, drhouse_s01e03, drhouse_s01e04, drhouse_s01e05, drhouse_s01e06, drhouse_s01e07,
    fellowshipofthering, twotowers, returnoftheking, thewitcher_s01e01, thewitcher_s01e02, thewitcher_s01e03]

tv_series = get_series()
movies = get_movies()
for series in tv_series:
    print('Serie: ', series)
for movie in movies:
    print('Movie: ', movie)

print('\n')
search('Return oF')

print('\n')
search('house')
