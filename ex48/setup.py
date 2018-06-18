try:
    from setuptoos import setup
except ImportError:

    config = {
        'description': 'Lexicon for acvanced user input.',
        'author': 'Jianyuan Bo',
        'author_email': 'ametrojan@gmail.com',
        'version': '0.1',
        'intall_requires': ['nose'],
        'packages': ['ex48'],
        'script': [],
        'name': 'ex48'
    }

setup(**config)
