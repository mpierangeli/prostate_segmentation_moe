# Metada needed for the library publishing

from setuptools import setup, find_packages

setup(
    name='your-library-name',  # Replace with the actual name of your library
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of your library',
    long_description=open('README.md').read(),  # Include a README file for a detailed description
    long_description_content_type='text/markdown',
    url='https://github.com/your-username/your-repository',  # Replace with your GitHub repository URL
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='your, library, keywords',
    project_urls={
        'Source': 'https://github.com/your-username/your-repository',
    },
)
