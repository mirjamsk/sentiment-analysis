import re
from utils.db_utils.sentiment_db import CommentEmojiSentimentDbConnection


class EmojiStats:

    def __init__(self, db_name="sentiment_db"):
        self.db = CommentEmojiSentimentDbConnection(db=db_name)
        self.db.connect()
        self.emoji_stats = self.get_emoji_stats()
        self.emoji_regex = self.get_emoji_regex()

    def get_emoji_stats(self):
        """
        emoji_stats = {
            ':)': {
                'neutral': 0.3,
                'positive': 0.3,
                'negative': 0.6,
                'sentiment_score': -0.2
            }
        }
        """
        emoji_stats = {}
        results = self.db.get_emoji_stats()
        for row in results:
            emoji = row[0]
            emoji_stats[emoji] = {
                'neutral': row[1],
                'positive': row[2],
                'negative': row[3],
                'sentiment_score': row[4]}
        return emoji_stats

    def get_emoji_regex(self):
        def sanitize_emojis(emojis):
            return emojis \
                .replace('(', '\(') \
                .replace(')', '\)') \
                .replace(':', '\:') \
                .replace('*', '\*') \
                .replace('-', '\-') \
                .replace('_', '\_') \
                .replace('.', '\.')

        emoji_regex = sanitize_emojis('|'.join(self.emoji_stats.keys()))
        emoji_regex = u'(' + emoji_regex + ')'

        return re.compile(emoji_regex)

    def find_emojis(self, text):
        emojis = self.emoji_regex.findall(text)
        print('Found emojis: %s' % (' '.join(emojis)))
        return emojis

    def contains_emoji(self, text):
        return True if len(self.emoji_regex.findall(text)) else False

    def get_comment_emoji_stats(self, text):
        comment_emoji_stats = []
        comment_emojis = self.find_emojis(text)
        for emoji in comment_emojis:
            comment_emoji_stats.append(self.emoji_stats[emoji])
        return comment_emoji_stats

    def update_db(self, comment_id, column, value):
        self.db.update(
            comment_id=comment_id,
            column=column,
            value=value)

    def close_db_connection(self):
        self.db.close()
