import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='gurupy',
    version='0.5',
    author='Harvey Wargo',
    description=('Python Data Wrangler Modules for GuruFocus Stock API'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(include=['gurupy', 'gurupy.*']),
    url='https://github.com/harveywargo2/guru-wrangler-py',
    keywords='stock financials dividends gurufocus gurupy 10K',
    classifiers=['Programming Language :: Python'],
    install_requires=[
        'requests',
        'pandas'
    ]

)