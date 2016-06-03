from abc import ABCMeta as _ABCMeta, abstractmethod


class BaseSpam(object):
    __metaclass__ = _ABCMeta

    @abstractmethod
    def is_spam(self, content, comment_author, post_id):
        pass

    @abstractmethod
    def get_db_column(self, use_en):
        pass
