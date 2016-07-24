import os

from setuptools import setup

setup(name='django-contact-form',
      version='1.3.1',
      zip_safe=False, # eggs are the devil.
      description='Generic contact-form application for Django',
      long_description=open(os.path.join(os.path.dirname(__file__),
                                         'README.rst')).read(),
      author='Maru Berezin',
      url='https://github.com/maru/django-contact-form/',
      packages=['contact_form', 'contact_form.tests'],
      package_data={'contact_form': [ 'locale/*/*/*',
            'templates/contact_form/*.html', 'templates/contact_form/*.txt']},
      test_suite='contact_form.runtests.run_tests',
      install_requires=['django-recaptcha==1.0.5'],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Framework :: Django :: 1.8',
                   'Framework :: Django :: 1.9',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Topic :: Utilities'],
      )
