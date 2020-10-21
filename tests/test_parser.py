from flore.parser import Parser


def test_sql_parser_with_required_varchar_unique():
    table_name = "users"
    columns = {"email": ["required", "varchar:120", "unique"]}
    parse = Parser().parse(table_name, columns)
    assert (
        parse
        == "CREATE TABLE if not exists users (email not null varchar(120) unique);"
    )
