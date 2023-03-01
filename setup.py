from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='fronty',
    version='0.0.2',
    description='A frontend web framework',
    long_description_content_type='text/markdown',
    long_description=long_description,
    author='Almas Ali',
    author_email='almaspr3@gmail.com',
    url='https://github.com/Almas-Ali/fronty',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='web framework',
    python_requires='>=3.10',

    entry_points={
        'console_scripts': [
            'fronty=fronty.cli:main',
        ],
    },
)
