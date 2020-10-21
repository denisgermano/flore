from flore.table import compose



def test_sql_parser_with_required_varchar_unique():
    table_name = "users"
    columns = {"email": ["required", "varchar:120", "unique"], "is_admin": ["required", "boolean"]}
    parse = compose(table_name, columns)
    assert (
        parse
        == 'CREATE TABLE if not exists users (email not null varchar(120) unique, is_admin not null boolean);'
    )
