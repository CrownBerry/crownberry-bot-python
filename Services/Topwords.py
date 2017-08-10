import operator


class Topwords:
    dictionary = {}

    def __init__(self):
        self.dictionary = {'all': {}}

    def add_word(self, word, user):
        if user not in self.dictionary:
            self.dictionary[user] = {}
            self.dictionary[user][word] = 1
        else:
            if word not in self.dictionary[user]:
                self.dictionary[user][word] = 1
            else:
                self.dictionary[user][word] += 1
        if word not in self.dictionary['all']:
            self.dictionary['all'][word] = 1
        else:
            self.dictionary['all'][word] += 1

    def get_topword(self, user):
        try:
            topword = max(self.dictionary[user].items(), key=operator.itemgetter(1))[0]
            times = self.dictionary[user][topword]
            return "Topword of " + user + " user is: " + topword + ", " + times + " times"
        except:
            return "There is no user with " + user + " username"
