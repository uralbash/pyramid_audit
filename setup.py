import os

from setuptools import find_packages, setup

this = os.path.dirname(os.path.realpath(__file__))


def read(name):
    with open(os.path.join(this, name)) as f:
        return f.read()

setup(
    name='pyramid_audit',
    version='0.0.1',
    url='http://github.com/ITCase/pyramid_audit/',
    author='Svintsov Dmitry',
    author_email='sacrud@uralbash.ru',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite="nose.collector",
    license="MIT",
    description='Mixin for audit user action in DB',
    long_description=read('README.rst'),
    install_requires=read('requirements.txt'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Framework :: Pyramid ",
        "Topic :: Internet",
        "Topic :: Database",
        'License :: OSI Approved :: MIT License',
    ],
)
