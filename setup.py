from setuptools import setup, find_packages

setup(
    name='mental-trade',  # Replace with your own package name
    version='0.1.0',
    author='Your Name',  # Replace with your own name
    author_email='your.email@example.com',  # Replace with your own email
    description='A brief description of your package',
    long_description=open('README.md').read(),  # Assuming you have a README file
    long_description_content_type='text/markdown',
    url='https://github.com/mcgabrielanthony-afk/mental-trade',  # Replace with your own URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # List your project's dependencies here
        'numpy',
        'pandas',
    ],
)