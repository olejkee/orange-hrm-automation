class Base():
    def __init__(self, driver):
        self.driver = driver

    @property
    def current_url(self):
        return self.driver.current_url
        
    def assert_url(self, expected_url):
        assert self.current_url == expected_url, \
            f"Expected URL to be {expected_url}, but was {self.current_url}"

    def assert_word(self, actual_word, expected_word):

        assert actual_word == expected_word, \
            f"Expected word to be '{expected_word}', but was '{actual_word}'"