import unittest
from MeshNode import MeshNode


class MeshNodeTest(unittest.TestCase):
    def setUp(self):
        self.mesh_node = MeshNode("Id")

    def tearDown(self):
        del self.mesh_node

    def testSeparateString(self):
        string_input = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        output_string = self.mesh_node.SeparateString(string_input)
        print(f"String Input: {string_input}\n")
        print(f"String Output: {output_string}\n")

        assert len(output_string) == 3
        assert len(output_string[0]) == self.mesh_node.max_string_size
        assert len(output_string[1]) == self.mesh_node.max_string_size
        assert len(output_string[2]) == len(string_input)  - 2*self.mesh_node.max_string_size

    def testCreatePacket(self):
        string_input = ''
        # Max String Size
        for i in range(self.mesh_node.max_string_size):
            string_input += 'a'
        print(len(string_input))
        self.mesh_node.CreatePacket(string_input)



if __name__ == '__main__':
    unittest.main()



