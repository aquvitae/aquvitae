from setuptools import setup, find_packages

setup(
    name='aquvitae',
    version='dev-0.1',
    description='The easiest Knowledge Distillation library for Light Weight DeepLearning',
    author='marload',
    author_email='rladhkstn8@gmail.com',
    url='https://github.com/aquvitae/aquvitae',
    download_url='https://github.com/aquvitae/aquvitae/archive/0.0.tar.gz',
    install_requires=[
        'tensorflow',
        'pytorch'
    ],
    packages=find_packages(exclude=[]),
    keywords=[
        'aquvitae',
        'deep-learning',
        'machine-learning',
        'light-weight',
        'knowledge-distillation'
    ],
    python_requires='>=3',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)