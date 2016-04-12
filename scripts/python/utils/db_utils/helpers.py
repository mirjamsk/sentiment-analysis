"""
 tiny helper methods for all things database
"""


def build_where_clause(id_equals='', id_greater_than='', id_less_than=''):
    where_clause = ''
    if id_equals is not None:
        where_clause = 'id=%d' % id_equals
    else:
        if id_less_than is not None:
            where_clause = 'id < %d' % id_less_than
        if id_greater_than is not None:
            where_clause += ' AND ' if where_clause != '' else ''
            where_clause += 'id > %d' % id_greater_than

    return where_clause
