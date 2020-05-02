class User:
    """User Object"""
    def createAccount(self, username: str, password: str, BMI: float):
        """
        Create a Wearther User

        `param` username: desired username

        `param` password: desired password

        `param` BMI: Height/Weight from frontend

        `return` confirmation of successful account creation
        """
    def updatePreferences(self, CSRF: str, preference: dict):
        """
        Update Weather User Preferences
        `param` CSRF: token of the currently logged in user

        `param` preference: key value pair where key is the attribute to be updated and value is the value it should be updated to.

        `return` confirmation of successful updating of user preferences.
        """
    def loginUser(self, username: str, password: hash):
        """
        Log user into weather and create a corresponding session.

        `param` username: the username of the existing user

        `param` password: the hashed password of the user.

        `return` Authorized CSRF token
        """
    def logoutUser(self, CSRF: str):
        """
        Log out current user from logged in session.

        `param` CSRF: token of the currently logged in user

        `return` Succesful deauthorization of CSRF token on server.
        """

class ClothingArticle:
    """Clothing article object"""

class Closet:
    """Closet object"""


def getClothingRecomendation(UserId: str, CSRF: str, location: dict):
    """
    Retrieve clothing based on forecast of current location and user preferences

    `param` UserId: The ID of the current User

    `param` CSRF: token of currently logged in user

    `param` location: location of user expressed as zip code or coordinate pair.

    `return` outfit recommendation
    """
    pass

def getUserByName(UserId: str):
    """
    Retrieve User by username.

    `param` UserId: ID of user in wearther

    `return` public facing data corresponding with UserId or 404.
    """
    pass

def getArticlefromClosetById(articleId: str):
    """
    Find and retrieve article of clothing by articleId if it exists.

    `param` articleId:

    `return` Corresponding clothing Article in closet or 404.
    """

def addClothingArticle(ClothingArticle):
    """

    `return` Successful article creation or 401.
    """
    pass

def getArticlefromClosetById(articleId: str):
    """
    Find a clothing article in wearther by its ID.

    `param` articleId: ID of clothing article in wearther

    `return` Corresponding clothing article in closet or 404.
    """

def findArticleByStatus(status: str, articleId: str, CSRF: str):
    """
    Find clothing article by status of either available or unavailable.

    `param` status:

    `param` articleId: ID of clothing article in wearther

    `return` Boolean representing the availability of the given clothing article.
    """

def findArticlesByTags(tag: str, CSRF: str):
    """
    Find clothing articles by type

    `param` tag: type of clothing article

    `param` CSRF: token of the currently logged in user

    `return`
    """

def getArticleById(articleId: str):
    """
    `param` articleId: ID of clothing article in wearther

    `return` Corresponding clothing article or 404.
    """

def uploadImage(Image: bytearray, CSRF: str):
    """
    Upload an image of an article of clothing.

    `param` Image: bytearray representing image

    `param` CSRF: token of currently logged in user

    `return` Confirmation of successful image upload or 401.
    """
def requestWeather(WSAPIParser, UserLocation: list):
    """
    Asks a Weather Service API Parser for a Weather object compiled by that weather service.
    `param` WSAPIParser:

    `param` UserLocation: list containing latitude longitude coordinate pair describing user's location

    `return` Request to Weather Service API parser
    """
def chooseWeatherService(UserLocation: list):
    """
    Chooses a weather service to get weather data from.
    `param` UserLocation: list containing latitude longitude coordinate pair describing user's location

    `return` Weather Service API Parser
    """
def getWeather(Location: list):
    """
    Get the weather data from a weather service.
    `param` Location: list containing latitude longitude coordinate pair describing location forecast is retrieved for

    `return` Weather Object
    """

def getLocationFromZipCode(zipcode: int):
    """

    :param zipcode: the 5 digit zip code
    :return: list containing latitude longitude coordinate pair.
    """

def isAvailable():
    """
    Determine if this weather service API is usable.

    `return` Boolean representing the availability of this Weather Service API Parser.
    """