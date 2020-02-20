

def write(file_name, libs):
    """
    param libs: list of libraries
    """

    with open(file_name, 'w') as f:
        f.write(f'{len(libs)}\n')
        for lib in libs:
            f.write(f'{lib.idx} {len(lib.books)}\n')
            f.write(f'{" ".join(str(l) for l in lib.books)}\n')
