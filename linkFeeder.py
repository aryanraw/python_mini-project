def file_to_list(filename):
    with open(filename, 'r') as f:
        links = f.readlines()
        # Remove any newline characters
        links = [link.strip() for link in links]
    return links