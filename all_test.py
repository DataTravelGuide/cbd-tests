#!/usr/bin/env python3

import sys

from avocado.core.job import Job
from avocado.core.suite import TestSuite

xfstests_config = {'resolver.references': ['xfstests.py:Xfstests.test'],
          'yaml_to_mux.files': ['xfstests.py.data/xfstests.yaml'],
          'nrunner.max_parallel_tasks': 1,
          'run.dry_run.enabled': False}

fio_config = {'resolver.references': ['fio.py:Fiotest.test'],
          'yaml_to_mux.files': ['fio.py.data/fio.yaml'],
          'nrunner.max_parallel_tasks': 1,
          'run.dry_run.enabled': False}

#upgradeonline_config = {'resolver.references': ['upgradeonline.py:Upgradeonlinetest.test'],
#          'yaml_to_mux.files': ['upgradeonline.py.data/upgradeonline.yaml'],
#          'nrunner.max_parallel_tasks': 1,
#          'run.dry_run.enabled': False}

test_suites = []

#test_suites.append(TestSuite.from_config(upgradeonline_config, name='upgradeonline'))
test_suites.append(TestSuite.from_config(xfstests_config, name='xfstests'))
test_suites.append(TestSuite.from_config(fio_config, name='fio'))

with Job(test_suites=test_suites) as j:
    sys.exit(j.run())
