import random

# DEBUG = True
#
# def noop(condition):
#     def decorator(f):
#         return (lambda *_, **__: None) if condition else f
#     return decorator
#
# @noop(DEBUG)
# def feature():
#     print('sadfg')
#     return 5
#
# print(feature())


class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.playbacks = 0

    def __str__(self):
        return f'{self.title} ({self.year})'

    __repr__ = __str__

    def play(self, value=1):
        self.playbacks += value


class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f'{self.title} S{self.season:0>2d}E{self.episode:0>2d}'

    __repr__ = __str__


def as_sorted(f):
    def wrapper(*args, **kwargs):
        return sorted(f(*args, **kwargs), key=lambda x: x.title, reverse=True)
    return wrapper


class Library:
    def __init__(self, titles):
        self.titles = [*titles]

    @as_sorted
    def get_series(self):
        return [title for title in self.titles if isinstance(title, Series)]

    @as_sorted
    def get_movies(self):
        return [title for title in self.titles if not isinstance(title, Series)]

    @as_sorted
    def search(self, phrase):
        return [title for title in self.titles if phrase.lower() in title.title.lower()]

    def generate_views(self):
        title = random.choice(self.titles)
        title.play(random.randrange(1, 100))

    def randomize_titles(self):
        for _ in range(10):
            self.generate_views()

    def top_titles(self):
        most_common = sorted(self.titles, key=lambda x: x.playbacks, reverse=True)
        for title in most_common:
            print(f'{title} {title.playbacks}')


if __name__ == '__main__':
    library = Library([
        Movie(title='Return of the Jedi', year=1979, genre='Science Fiction'),
        Movie(title='Fellowship of the Ring', year=2002, genre='Fantasy'),
        Movie(title='The Two Towers', year=2003, genre='Fantasy'),
        Movie(title='Return of the King', year=2004, genre='Fantasy'),
        Series(title='Dr House', year=2010, genre='drama', season=1, episode=1),
        Series(title='Dr House', year=2010, genre='drama', season=1, episode=2),
        Series(title='Dr House', year=2010, genre='drama', season=1, episode=3),
        Series(title='Dr House', year=2010, genre='drama', season=1, episode=4),
        Series(title='Dr House', year=2010, genre='drama', season=1, episode=5),
        Series(title='Dr House', year=2010, genre='drama', season=1, episode=6),
        Series(title='Dr House', year=2010, genre='drama', season=1, episode=7),
        Series(title='The Witcher', year=2019, genre='fantasy', season=1, episode=1),
    ])
    library.titles.append(Series(title='The Witcher', year=2019, genre='fantasy', season=1, episode=3))
    print(library.search('cher'))


# library = Library()
# for item in library.get_series():
#     print(item)
# print('\n')
# for item in library.get_movies():
#     print(item)
# print('\n')
# library.search('house')
# library.randomize_titles()
# print('\n')
# library.top_titles()

# print('\n')
# search('Return oF')
#
# print('\n')
# search('house')
#
# randomize_titles()
#
# print('\n')
# top_titles()
