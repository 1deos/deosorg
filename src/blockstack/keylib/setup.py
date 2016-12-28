"""
Keylib
==============

"""

from setuptools import setup, find_packages

setup(
    name='keylib',
    version='0.1.0',
    url='https://github.com/blockstack/keylib-py',
    license='MIT',
    author='Blockstack Developers',
    author_email='hello@onename.com',
    description="""Library for creating and working with private keys, public keys, and bitcoin addresses.""",
    keywords='public private key elliptic curve ecdsa secp256k1 cryptography bitcoin',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'requests>=2.9.1',
        'ecdsa>=0.13',
        'utilitybelt>=0.2.6'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)