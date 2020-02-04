class News:
    """
    News class to define News Objects
    """

    def __init__(self, id, title, description, url, urlToImage, ):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage


class Sources:
    def __init__(self, id, name, description, url, category, language, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
