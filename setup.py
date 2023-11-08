import setuptools

setuptools.setup(
    name='gurupy',
    version='0.3',
    author='Harvey Wargo',
    packages=setuptools.find_packages(include=['gurupy' , 'gurupy.*']),
    url='https://github.com/harveywargo2/guru-wrangler-py',
    keywords='stock financials dividends gurufocus',
    install_requires=[
        'requests'
    ]

)