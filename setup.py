from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2',
]

setup(
    name='First-Flask-App',
    version='0.0.0',
    description='Just messing around with Flask.',
    author='Ryan French',
    author_email='rafrench@svsu.edu',
    keywords='flask',
    packages=find_packages()
    include_package_data=True,
    install_requires=requires
)
