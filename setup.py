from pathlib import Path

from setuptools import setup, find_packages

PARENT_DIR = Path(__file__).resolve(strict=True).parent


def get_version():
    """Generate new version for project"""
    with open(PARENT_DIR / 'version') as f:
        version = f.readline()
        return version


setup(
    name="djgraphql",
    version=get_version(),
    license="file: LICENSE.txt",
    description="A package that makes easier to use graphql with django.",
    long_description="file: README.md",
    url="https://shitalluitel.com.np",
    author="Shital Babu Luitel",
    author_email="ctalluitel@gmail.com",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    include_package_data=True,
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        'django==3',
        'graphene-django',
    ],
)
