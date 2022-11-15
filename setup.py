#!/usr/bin/env python3

from setuptools import setup
from setuptools.command.build_py import build_py
from setuptools.command.develop import develop


try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

    class bdist_wheel(_bdist_wheel):

        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            # Mark us as not a pure python package
            self.root_is_pure = False

        def get_tag(self):
            python, abi, plat = _bdist_wheel.get_tag(self)
            # We don't link with python ABI, but require python3
            python, abi = 'py3', 'none'
            return python, abi, plat
except ImportError:
    bdist_wheel = None


long_description = "This package makes the [Temporal Fast Downward](http://gki.informatik.uni-freiburg.de/tools/tfd/) planning system available in the [unified_planning library](https://github.com/aiplan4eu/unified-planning) by the [AIPlan4EU project](https://www.aiplan4eu-project.eu/)."

setup(name='up_tfd',
      version='0.0.1',
      description='Unified Planning Integration of the Temporal Fast Downward planning system',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Davide Lusuardi',
      author_email='davide.lusuardi@studenti.unitn.it',
      url='', # TODO
      classifiers=['Development Status :: 1',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                   'Programming Language :: Python :: 3',
                   'Topic :: Scientific/Engineering :: Artificial Intelligence'
                   ],
      packages=['up_tfd'],
    #   package_data={
    #       "": ['fast_downward.py', 'downward/fast-downward.py',
    #           'downward/README.md', 'downward/LICENSE.md',
    #           'downward/builds/release/bin/*',
    #           'downward/builds/release/bin/translate/*',
    #           'downward/builds/release/bin/translate/pddl/*',
    #           'downward/builds/release/bin/translate/pddl_parser/*',
    #           'downward/driver/*', 'downward/driver/portfolios/*']
    #   },
      package_data={ # TODO
        "": ['tfd.py']
      },
      cmdclass={
          'bdist_wheel': bdist_wheel,
          'build_py': build_py,
          'develop': develop,
      },
      has_ext_modules=lambda: True
      )
