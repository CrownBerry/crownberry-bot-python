import operator


class Topwords:
    dictionary = {}

    def __init__(self):
        self.dictionary = {'all': {'': 0}}

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
        if user in self.dictionary:
            topword = max(self.dictionary[user], key=self.dictionary[user].get)
            times = self.dictionary[user][topword]
            return "Topword of " + user + " user is: " + topword + ", " + str(times) + " times"
        else:
            return "There is no user with " + user + " username"
