import argparse
import utils.db_utils.helpers as db_helpers


class CommentArgumentParser(object):
    def __init__(self, description=''):
        self.args = None
        self.where_clause = ''
        self.parser = argparse.ArgumentParser(description=description)

        self.parser.add_argument(
            '-ideq',
            type=int,
            required=False,
            help='Update a specific comment by specifying it\'s id')

        self.parser.add_argument(
            '-idlt',
            type=int,
            required=False,
            help='Update all comments with id less than the specified id')

        self.parser.add_argument(
            '-idgt',
            type=int,
            required=False,
            help='Update all comments with id greater than the specified id')

    def parse_args(self):
        self.args = self.parser.parse_args()
        self.where_clause = db_helpers.build_where_clause(
            id_equals=self.args.ideq,
            id_less_than=self.args.idlt,
            id_greater_than=self.args.idgt)

    def add_argument(self, arg_name, type, required, help):
        self.parser.add_argument(
            arg_name,
            help=help,
            type=type,
            required=required)

    def add_argument_with_choices(self, arg_name, choices, required, help):
        self.parser.add_argument(
            arg_name,
            help=help,
            choices=choices,
            required=required)
