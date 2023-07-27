from setuptools import setup, find_packages

setup(
	name='downloadify',
	version='1.0.0',
	description='Download your spotify playlists and songs easily, store them in any folder you want, and even in your phone',
    author='kzt',
    author_email='gustavoasc2004@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.11.3',
    ],
)
