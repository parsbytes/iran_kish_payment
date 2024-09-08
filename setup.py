from setuptools import setup, find_packages

setup(
    name="iran_kish_payment",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'pycryptodome',
        'requests',
        'urllib3<2'
    ],
    tests_require=[
        'unittest',
    ],
    test_suite='tests',
    description="Iran Kish payment portal",
    author="parsbytes",
    author_email="parsbytes@gmail.com",
    url="https://github.com/parsbytes/iran_kish_payment",
)
