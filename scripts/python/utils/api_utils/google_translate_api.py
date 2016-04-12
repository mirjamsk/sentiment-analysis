from base_api import BaseAPI


class GoogleTranslateAPI(BaseAPI):
    def __init__(self):
        self.language_column='language',
        self.english_tranalation_column='english_translation',
        BaseAPI.__init__(
            self,
            url='https://www.googleapis.com/language/translate/v2?key=AIzaSyDXYzpYdHG8W2sGxd7e_E_zpci4S7pQNTg',
            params={'target': 'en', 'q': ''}
        )

    def set_text(self, text):
        self.params['q'] = text

    def get_detected_language(self):
        return self.response.json()['data']['translations'][0]['detectedSourceLanguage']

    def get_translation(self):
        return self.response.json()['data']['translations'][0]['translatedText']

    def __str__(self):
        return self.__name__
