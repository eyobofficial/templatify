import re
import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument('filename')
def assets(filename):
    """Convert static link assets to support Django template."""
    pattern = r'''
                (src|href)=("|')
                (([-/.a-zA-Z0-9]+)\.(min\.)?(pdf|jpg|jpeg|png|gif|svg|css|js))  # Target filename
                ("|')
               '''
    regex = re.compile(pattern, re.VERBOSE)
    sub_regex_exp = r'''\1="{% static '\3' %}"'''
    with open(filename, 'r') as fh:
        lines = fh.readlines()
        with open(filename, 'w') as new_fh:
            for line in lines:
                line = regex.sub(sub_regex_exp, line)
                new_fh.write(line)


@cli.command()
@click.argument('filename')
def links(filename):
    """Convert internal hyperlinks to support Django templates."""
    pattern = r'''
                href=("|')
                ([-/.a-zA-Z0-9]+\.html)  # Target filename
                ("|')
               '''
    regex = re.compile(pattern, re.VERBOSE)
    sub_regex_exp = r'href="#"'
    with open(filename, 'r') as fh:
        lines = fh.readlines()
        with open(filename, 'w') as new_fh:
            for line in lines:
                line = regex.sub(sub_regex_exp, line)
                new_fh.write(line)


if __name__ == '__main__':
    cli()