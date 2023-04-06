import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='connmgr',
    version='0.0.1',
    author='Bart Verweire',
    author_email='bart.verweire@smals.be',
    description='Connection Manager for Smals databases',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://git.cloud.smals.be/database/transversal/dbconnectionmanager',
    project_urls = {
        "Bug Tracker": "https://git.cloud.smals.be/database/transversal/dbconnectionmanager/-/issues"
    },
    license='Smals Internal',
    packages=['connmgr'],
    install_requires=['pandas','sqlalchemy','oracledb','psycopg2'],
)