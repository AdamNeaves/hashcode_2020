

def write(file_name, libs):
    """
    param libs: list of libraries
    """
    with open(file_name, 'w') as f:
        f.write(f'{len(libs)}\n')
        for lib in libs:
            f.write(f'{lib.idx} {len(libs.books)}\n')
            f.write(f'{" ".join(lib.books)}\n')
