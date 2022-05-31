from collections import defaultdict
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


class TextProcess:

    def __init__(self):
        self.pos_tweets = defaultdict(int)
        self.neg_tweets = defaultdict(int)
        self.stem = PorterStemmer()
        self.remove_punc = RegexpTokenizer(r"\w+")
        self.stop_words = set(stopwords.words("english"))
        self.stop_words.add("user")
        self.total = 0
        print("Initialized Successfully")

    def __clean_text__(self, string):
        """
        Cleans 1 string at a time.
        :return Processed Tweet after removing
        Stop words, Punctuations, @user(specific), and do Stemming.
        """
        x = list(self.remove_punc.tokenize(string))
        processed_text = []
        for i in x:
            if i in self.stop_words:
                continue
            processed_text.append(self.stem.stem(i))
        return processed_text

    def extract_info(self, string, label):
        """
        Extract the info from string (1 at a time)
        and use that information to update pos/neg tweets value.
        """
        processed_text = self.__clean_text__(string)
        for i in processed_text:
            if label == 1:
                self.pos_tweets[i] += 1
            else:
                self.neg_tweets[i] += 1
        self.total += 1
        print("Extraction Number:", self.total)

    def extract_feature(self, texts):
        """
        Returns the feature value
        MUST BE CALLED AFTER EXTRACTING ALL THE INFO
        """
        vec = []
        for text in texts:
            extracted = set()
            pos_val, neg_val = 0, 0
            text = self.__clean_text__(text)
            for i in text:
                if i in extracted:
                    continue
                extracted.add(i)
                if i in self.pos_tweets:
                    pos_val += self.pos_tweets[i]
                if i in self.neg_tweets:
                    neg_val += self.neg_tweets[i]
            vec.append([1, pos_val, neg_val])
        return vec


if __name__ == "__main__":
    print("TextProcess Test run for the class")
    test = TextProcess()
    test.extract_info("@user hello #world this is me. Testing the result @hehehe", 1)
