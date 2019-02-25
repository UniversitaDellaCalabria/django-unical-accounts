from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='Django Unical Accounts',
      version='0.2',
      description="/home/wert/DEV3/pyWSArchiPRO/setup.py",
      long_description=readme(),
      classifiers=['Development Status :: 5 - Production/Stable',
                  'License :: OSI Approved :: BSD License',
                  'Programming Language :: Python :: 3 :: Only'],
      url='https://github.com/UniversitaDellaCalabria/django-unical-accounts',
      author='Giuseppe De Marco',
      author_email='giuseppe.demarco@unical.it',
      license='BSD',
      packages=['unical_accounts'],
      install_requires=[
                      'django>2.0,<2.1',
                      'django_countries'
                  ],
     )
