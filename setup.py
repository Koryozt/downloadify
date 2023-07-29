from setuptools import setup, find_packages

setup(
	name='downloadify',
	version='1.0.0',
	description='Download your spotify playlists with a single python script in any folder do you want',
    url='https://github.com/Koryozt/downloadify',
    author='kzt',
    author_email='gustavoasc2004@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'yt-dlp'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End-Users',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.11.3',
    ],
)
