from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


class ImageGenerator(object):
    """docstring for ImageGenerator"""

    def generate(self, word_str, height, width):

        stopwords = set(STOPWORDS)

        wordcloud = WordCloud(
            font_path='assets\\abc.otf',
            background_color='white',
            stopwords=stopwords,
            max_words=100,
            height=height,
            width=width,
            repeat=True,
            # random_state=1
        ).generate(str(word_str))
        try:
            wordcloud.to_file("Output.png")
            return True
        except:
            return False
