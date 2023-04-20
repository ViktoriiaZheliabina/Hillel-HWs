import xml.etree.ElementTree as ET


def get_movie_description(movie_title: str):
    """

    Args:
        movie_title: title of the movie

    Returns: movie description or None if movie is not found

    """
    tree = ET.parse("movies.xml")
    root = tree.getroot()
    for movie in root.iter('movie'):
        if movie.attrib['title'] == movie_title:
            description = movie.find('description').text
            print(description)
    return None

get_movie_description("Ferris Bueller's Day Off")




