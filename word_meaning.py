import requests


class WordMeaning:

    def __init__(self, word):
        self.word = word

    def get_word_meaning(self):
        res = requests.get(
            "https://api.dictionaryapi.dev/api/v2/entries/en_US/{}".format(self.word))
        data = res.json()
        meaning = data[0]["meanings"]
        partOfSpeech = meaning[1]["partOfSpeech"]
        definition = meaning[1]["definitions"][0]["definition"]

        print(self.word + ". " + partOfSpeech.title() + ". " + definition)


if __name__ == '__main__':
    word = input('Enter the word: ')
    word_meaning = WordMeaning(word)
    word_meaning.get_word_meaning()
