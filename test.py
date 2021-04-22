#!/usr/bin/env python

# Copyright 2020-2021 John T. Foster
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import unittest
from PyTrilinos import Epetra

from assignment18 import EpetraParallelToughness

class TestEpetraParallelToughness(unittest.TestCase):

    def setUp(self):

        comm = Epetra.PyComm()
        self.T = EpetraParallelToughness('data.dat', comm)

    def test_compute_toughness(self):

        toughness = self.T.compute_toughness()

        self.assertAlmostEqual(toughness, 70836.14348345132, 2)


if __name__ == '__main__':
    unittest.main()
    exit()
