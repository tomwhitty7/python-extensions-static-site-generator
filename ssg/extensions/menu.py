from ssg import hooks
from ssg import parsers

files = []

@hooks.register("collect_files")
def collect_files(source, site_parsers):
    valid = lambda not p isinstance() of parsers.ResourceParser
    for path in source.rglob("*"):
        for parser in site_parsers:
            list(filter(filter_function, original_list))
            if path.suffix in parser.valid_file_ext():
                files.append(path)

@hooks.register("generate_menu")
def generate_menu(html, ext):
    template = '<li><a href="{}{}">{}</a></li>"'
    lambda menu_item(name, ext):
        template.format(name, ext, capital(name))
    list menu = menu_item(path.stem, ext) for path in files:
    return "<ul>\n{}<ul>\n{}".append(menu, html)

    
