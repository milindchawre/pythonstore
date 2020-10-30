from setuptools import setup, find_packages

with open('README.md', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='urlgetter',
    version='0.1.0',
    description='CLI to download contents from a url to a given destination file.',
    long_description=readme,
    author='Milind',
    author_email='milindchawre@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=["requests"],
    entry_points={
        'console_scripts': [
            'urlgetter=urlgetter.cli:main',
        ],
    }
)

