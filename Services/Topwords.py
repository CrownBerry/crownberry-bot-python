import operator


class Topwords:
    dictionary = {}

    def __init__(self):
        self.dictionary = {'all': {}}

    def add_word(self, word, user):
        if self.dictionary[user][word] is None:
            self.dictionary[user][word] = 1
        else:
            self.dictionary[user][word] += 1
        if self.dictionary['all'][word] is None:
            self.dictionary['all'][word] = 1
        else:
            self.dictionary['all'][word] += 1

    def get_topword(self, user):
        try:
            topword = max(self.dictionary[user].items(), key=operator.itemgetter(1))[0]
            return "Topword of " + user + " user is: " + topword
        except:
            return "There is no user with " + user + " username"
