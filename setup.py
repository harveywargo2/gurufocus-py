from setuptools import setup, find_packages

setup(
    name='gurupy',
    version='0.2',
    author='Harvey Wargo',
    packages=find_packages(),
    url='https://github.com/harveywargo2/guru-wrangler-py',
    keywords='stock financials dividends gurufocus',
    install_requires=[
        'requests'
    ]

)