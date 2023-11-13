import setuptools


setuptools.setup(
    name='gurupy',
    version='0.3',
    author='Harvey Wargo',
    packages=setuptools.find_packages(include=['gurupy' , 'gurupy.*']),
    description=('Python Data Wrangler Modules for GuruFocus Stock API'),
    url='https://github.com/harveywargo2/guru-wrangler-py',
    keywords='stock financials dividends gurufocus gurupy 10K',
    install_requires=[
        'requests',
        'pandas'
    ]

)