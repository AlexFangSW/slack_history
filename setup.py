from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

with open("requirements.txt", "r") as file:
    install_requires = file.readlines()

version = {}
with open("src/slackhistory/version.py") as file:
    exec(file.read(), version)

setup(
    name="slackhistory",
    version=version['__version__'],
    author="Alex",
    author_email="alexfangsw@gmail.com",
    description=
    "A slack helper library to get history (messages and replies) of a channel",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/AlexFangSW/slack_history",
    package_dir={'': 'src'},
    packages=find_packages(where='src', exclude=['slackhistory.tests']),
    install_requires=install_requires,
    python_requires='>=3.11',
    keywords=["slackhistory", "slack history", "slack helper"])
