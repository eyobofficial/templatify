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
                (([-/.a-zA-Z0-9]+)\.(min\.)?(jpg|jpeg|png|gif|svg|css|js))  # target filename
                ("|')
               '''
    regex = re.compile(pattern, re.VERBOSE)
    sub_regex_exp = r'''\1="{% static '\3' %}"'''
    with open(filename, 'r') as fh:
        lines = fh.readlines()
        with open(filename, 'w') as new_fh:
            new_fh.write('{% load static %}\n')
            for line in lines:
                line = regex.sub(sub_regex_exp, line)
                new_fh.write(line)


if __name__ == '__main__':
    cli()