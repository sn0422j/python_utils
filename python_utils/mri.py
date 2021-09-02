import numpy as np


def vox2real(voxel_coords: np.ndarray, affine: np.ndarray) -> np.ndarray:
    """convert voxel space to real space with affine.

    Args:
        voxel_coords (np.ndarray): (N,3) coords array
        affine (np.ndarray): (4,4) affine array

    Raises:
        ValueError: the shape of coords should be (N,3).
        ValueError: the shape of affine should be (4,4).

    Returns:
        np.ndarray: converted coords
    """
    if not (voxel_coords.shape[1] == 3 and len(voxel_coords.shape) == 2):
        raise ValueError("the shape of coords should be (N,3).")
    if not affine.shape == (4, 4):
        raise ValueError("the shape of affine should be (4,4).")

    voxel_coords = np.vstack([np.transpose(voxel_coords), np.ones(len(voxel_coords))])
    return np.transpose(np.dot(affine, voxel_coords)[:3, :]).astype(np.float64)


def real2vox(real_coords: np.ndarray, affine: np.ndarray) -> np.ndarray:
    """onvert real space to voxel space with affine.

    Args:
        real_coords (np.ndarray): (N,3) coords array
        affine (np.ndarray): (4,4) affine array

    Raises:
        ValueError: the shape of coords should be (N,3).
        ValueError: the shape of affine should be (4,4).
        ValueError: affine inversion failed.

    Returns:
        np.ndarray: converted coords
    """

    if not (real_coords.shape[1] == 3 and len(real_coords.shape) == 2):
        raise ValueError("the shape of coords should be (N,3).")
    if not affine.shape == (4, 4):
        raise ValueError("the shape of affine should be (4,4).")

    real_coords = np.vstack([np.transpose(real_coords), np.ones(len(real_coords))])
    try:
        affine_inv = np.linalg.inv(affine)
    except:
        raise ValueError("inverse affine could not be computed.")
    return np.transpose(np.dot(affine_inv, real_coords)[:3, :]).astype(np.float64)
