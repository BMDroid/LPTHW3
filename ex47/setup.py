try:
    from setuptoos import setup
except ImportError:

    config = {
        'description': 'The ex47 for the lpthw, and this is the project to learn the Automated Testing.',
        'author': 'Jianyuan Bo',
        'author_email': 'ametrojan@gmail.com',
        'version': '0.1',
        'intall_requires': ['nose'],
        'packages': ['ex47'],
        'script': [],
        'name': 'ex47'
    }

setup(**config)
