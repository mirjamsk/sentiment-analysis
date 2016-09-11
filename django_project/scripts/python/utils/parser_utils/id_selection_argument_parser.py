import argparse
import utils.db_utils.helpers as db_helpers


class IdSelectionArgumentParser(object):
    def __init__(self, description=''):
        self.args = None
        self.id_selection = ''
        self.parser = argparse.ArgumentParser(description=description)

        self.parser.add_argument(
            '-ideq',
            type=int,
            nargs='+',
            required=False,
            help='run for records by specifying their ids')

        self.parser.add_argument(
            '-idlt',
            type=int,
            required=False,
            help='run for records with id less than the specified id')

        self.parser.add_argument(
            '-idgt',
            type=int,
            required=False,
            help='run for records with id greater than the specified id')

    def parse_args(self):
        self.args = self.parser.parse_args()
        self.id_selection = db_helpers.build_id_selection_condition(
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

    def add_mutually_exclusive_group(self, required=True):
        return self.parser.add_mutually_exclusive_group(required=required)
