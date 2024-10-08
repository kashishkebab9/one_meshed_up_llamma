import unittest
from MeshNode import MeshNode


class MeshNodeTest(unittest.TestCase):
    def setup(self):
        self.mesh_node = MeshNode("Id")

    def tearDown(self):
        del self.mesh_node

    def testCreatePacket(self):
        # TODO: Test for Type Correction
        # TODO: Test for Size (input and output)
