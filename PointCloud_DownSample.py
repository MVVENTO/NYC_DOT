import numpy as np
import open3d
import pye57

point_file = "Z:\Administrative_Guide\PMA\Melissa Vento\PART 1\Point Clouds\Point Cloud Files (.e57)/path/to/181692.31_GerritsenBeach_PART1_Noel Ct.e57"

e57 = pye57.E57(point_file)
data = e57.read_scan_raw(0)
assert isinstance(data["cartesianX"], np.ndarray)
assert isinstance(data["cartesianY"], np.ndarray)
assert isinstance(data["cartesianZ"], np.ndarray)

x = np.array(data["cartesianX"])
y = np.array(data["cartesianY"])
z = np.array(data["cartesianZ"])

pcd_points = np.concatenate((x, y), axis=0)
pcd_points = np.concatenate((pcd_points, z), axis=0)
pcd_points = velo_points.reshape(-1, 3)

pcd = open3d.geometry.PointCloud()
pcd.points = open3d.utility.Vector3dVector(pcd_points)
pcd_down = pcd.voxel_down_sample(voxel_size=0.0035)
