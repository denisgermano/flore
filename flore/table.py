from .normalize import normalize


def compose(table_name, columns):
    tables = ''
    for name, fields in columns.items():
        text =  normalize(fields)
        tables += "%s %s, " %(name, text)

    return mount(table_name, tables)


def mount(table_name, tables):
    table = "CREATE TABLE if not exists {0} ({1});".format(table_name, tables)
    return table.replace(", )", ")")
