from setuptools import setup, find_packages
from AminoLab.__init__ import __version__

with open("README.md", "r") as stream:
    long_description = stream.read()

setup(
    name = 'AminoLab',
    version = __version__,
    url = 'AKATSKI AMINO BY SFAH',
    download_url = 'https://t.me/spi22der',
    license = 'SFAH',
    author = 'Kratos',
    author_email = 'dyam1487@gmail.com',
    description = .'BSAMINO PILUS ',
    long_description_content_type = 'text/markdown',
    keywords = [
        'aminoapps',
        'amino-py',
        'amino',
        'amino-bot',
        'narvii',
        'api',
        'python',
        'python3',
        'python3.x',
        'lilzevi',
        'botamino',
        'aminoapp'
    ],
    install_requires = [
        'setuptools',
        'requests',
    ],
    setup_requires = [
        'wheel'
    ],
    packages = find_packages()
)
