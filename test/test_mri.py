import unittest
import sys
from pathlib import Path
import numpy as np

sys.path.append(str(Path(__file__).resolve().parent.parent))
from python_utils.mri import vox2real, real2vox


class TestVoxReal(unittest.TestCase):
    def test_vox2real_real2vox(self):
        affine = np.asarray(
            [
                [1, 1, 3, 0],
                [0, 2, 0, 0],
                [4, 2, 1, 0],
                [0, 0, 0, 1],
            ],
            dtype=np.float64,
        )
        voxel_coords = np.asarray([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=np.float64)
        real_coords = np.asarray(
            [[12.0, 4.0, 11.0], [27.0, 10.0, 32.0]], dtype=np.float64
        )
        self.assertTrue(np.allclose(real_coords, vox2real(voxel_coords, affine)))
        self.assertTrue(np.allclose(voxel_coords, real2vox(real_coords, affine)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
