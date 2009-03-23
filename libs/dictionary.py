
class YahooDictionary:

    url = "http://tw.dictionary.yahoo.com/search?ei=UTF-8&p=%s"

    @staticmethod
    def get_search_url(word):
        """
        get query url of the yahoo dictionary.

        >>> YahooDictionary.get_search_url('hi')
        "http://tw.dictionary.yahoo.com/search?ei=UTF-8&p=hi"
        """   
        return YahooDictionary.url % word
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
