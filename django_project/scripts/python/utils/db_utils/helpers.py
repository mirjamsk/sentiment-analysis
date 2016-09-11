"""
 tiny helper methods for all things database
"""


def build_id_selection_condition(id_equals=[], id_greater_than='', id_less_than=''):
    where_clause = ''
    if id_equals is not None:
        id_equals = '(' + ', '.join([str(id) for id in id_equals]) + ')'
        where_clause = 'id in %s' % id_equals
    else:
        if id_less_than is not None:
            where_clause = 'id < %d' % id_less_than
        if id_greater_than is not None:
            where_clause += ' AND ' if where_clause != '' else ''
            where_clause += 'id > %d' % id_greater_than

    return where_clause
