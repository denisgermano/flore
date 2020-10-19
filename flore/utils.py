def open_yaml_file(filename):
    with open(f"migrations/{filename}.yaml", mode="r") as f:
        return f.read()
