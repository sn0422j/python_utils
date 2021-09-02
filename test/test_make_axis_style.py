import unittest
import os
import sys
from pathlib import Path
import matplotlib.pyplot as plt

sys.path.append(str(Path(__file__).resolve().parent.parent))
from python_utils.plotting import make_axis_style


def test_make_axis_style():
    fig, axis = plt.subplots(1, 1)
    axis.set(
        **make_axis_style(
            xlim=[0, 1],
            ylim=[0, 1],
            xlabel="xlabel",
            ylabel="ylabel",
            title="title",
            xticks=[0.0, 0.25, 0.5, 0.75, 1],
            yticks=[0.0, 0.25, 0.5, 0.75, 1],
            xticklabels=["0", "1/4", "1/2", "3/4", "1"],
            yticklabels=["0", "1/4", "1/2", "3/4", "1"],
        )
    )
    os.makedirs("./outputs", exist_ok=True)
    fig.savefig("./outputs/test.png", bbox_inches="tight")


if __name__ == "__main__":
    test_make_axis_style()


class TestAxis(unittest.TestCase):
    def test_make_axis_style(self):
        fig, axis = plt.subplots(1, 1)
        style_dict = make_axis_style(
            xlim=[0, 1],
            ylim=[0, 1],
            xlabel="xlabel",
            ylabel="ylabel",
            title="title",
            xticks=[0.0, 0.25, 0.5, 0.75, 1],
            yticks=[0.0, 0.25, 0.5, 0.75, 1],
            xticklabels=["0", "1/4", "1/2", "3/4", "1"],
            yticklabels=["0", "1/4", "1/2", "3/4", "1"],
        )
        self.assertIsInstance(style_dict, dict)
        axis.set(**style_dict)
        os.makedirs("./outputs", exist_ok=True)
        fig.savefig("./outputs/test.png", bbox_inches="tight")
        self.assertTrue(os.path.isfile("./outputs/test.png"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
