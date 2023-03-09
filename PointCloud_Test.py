# Author: Melissa A Vento
# Date: 07/13/2022
# Description: Neural Network Program - Machine learning script that automates asset collection of street ends 

#    Step 1 : Annotate pointclouds       Location ->  Z:\Administrative_Guide\PMA\Melissa Vento\PART 1\Point Clouds
#    Step 2 : Load Data
#    Step 3 : Preprocess Data
#    Step 4 : Augmentation
#               Train Model
#                    Algorithm choices -> Convolutional Neural Network
#                                         Point Pillars Network
#                                         PointNet 
#   Step 5 : Test Model -> verify accuracy  



# pip install open3d 


import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt




print("Load a ply point cloud, print it, and render it")
ply_point_cloud = o3d.data.PLYPointCloud()
pcd = o3d.io.read_point_cloud(ply_point_cloud.path)
print(pcd)
print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd],
                                  zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])


######### read image ##########

print("Testing IO for images ...")
img = o3d.io.read_image("Z:\Administrative_Guide\PMA\Melissa Vento\PART 1\Imagery\Abbey Ct\DJI_20220316134000_0009.JPG")
print(img)
o3d.io.write_image("copy_of_Abbey.jpg", img)





print("Load a polygon volume and use it to crop the original point cloud")
demo_crop_data = o3d.data.DemoCropPointCloud()
pcd = o3d.io.read_point_cloud(demo_crop_data.point_cloud_path)
vol = o3d.visualization.read_selection_polygon_volume(demo_crop_data.cropped_json_path)
chair = vol.crop_point_cloud(pcd)
o3d.visualization.draw_geometries([chair],
                                  zoom=0.7,
                                  front=[0.5439, -0.2333, -0.8060],
                                  lookat=[2.4615, 2.1331, 1.338],
                                  up=[-0.1781, -0.9708, 0.1608])



import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt

############## Crop original point cloud #########

print("Load a polygon volume and use it to crop the original point cloud")
demo_crop_data = o3d.data.DemoCropPointCloud()
pcd = o3d.io.read_point_cloud(demo_crop_data.point_cloud_path)
vol = o3d.visualization.read_selection_polygon_volume(demo_crop_data.cropped_json_path)
chair = vol.crop_point_cloud(pcd)
o3d.visualization.draw_geometries([chair],
                                  zoom=0.7,
                                  front=[0.5439, -0.2333, -0.8060],
                                  lookat=[2.4615, 2.1331, 1.338],
                                  up=[-0.1781, -0.9708, 0.1608])


################ bounding bloxes over point cloud image ##############

aabb = chair.get_axis_aligned_bounding_box()
aabb.color = (0.5,0,0.6)
obb = chair.get_oriented_bounding_box()
obb.color = (0.7,1,0.1)
o3d.visualization.draw_geometries([chair, aabb, obb],
                                  zoom=0.7,
                                  front=[0.5439, -0.2333, -0.8060],
                                  lookat=[2.4615, 2.1331, 1.338],
                                  up=[-0.1781, -0.9708, 0.1608])


########## paint point cloud image ############

print("Paint chair")
chair.paint_uniform_color([0.1,0.8,0.8 ])
o3d.visualization.draw_geometries([chair],
                                  zoom=0.7,
                                  front=[0.5439, -0.2333, -0.8060],
                                  lookat=[2.4615, 2.1331, 1.338],
                                  up=[-0.1781, -0.9708, 0.1608])


###########  read and display PLY point clouds in Python ###########
'''
pip install open3d

import numpy as np
from open3d import *    

def main():
    cloud = read_point_cloud("cloud.ply") # Read the point cloud
    draw_geometries([cloud]) # Visualize the point cloud     

if __name__ == "__main__":
    main()



import numpy as np
import open3d
from open3d import *    
from open3d import read_point_cloud

def main():
    cloud = read_point_cloud("Z:\Administrative_Guide\PMA\Melissa Vento\PART 1\Point Clouds\Point Cloud Files (.e57)/path/to/181692.31_GerritsenBeach_PART1_Noel Ct.e57") # Read the point cloud
    draw_geometries([cloud]) # Visualize the point cloud     

if __name__ == "__main__":
    main()


'''
################ Downsampling point cloud #############

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



########### Lidar labeling pointcloud ##########
# jupiter notebook command 
'''
pip install labelCloud

labelCloud

labelCloud --example
'''


######### isolate target area ###########
# remove chair from background


# Load data
demo_crop_data = o3d.data.DemoCropPointCloud()
pcd = o3d.io.read_point_cloud(demo_crop_data.point_cloud_path)
vol = o3d.visualization.read_selection_polygon_volume(demo_crop_data.cropped_json_path)
chair = vol.crop_point_cloud(pcd)

dists = pcd.compute_point_cloud_distance(chair)
dists = np.asarray(dists)
ind = np.where(dists > 0.01)[0]
pcd_without_chair = pcd.select_by_index(ind)
o3d.visualization.draw_geometries([pcd_without_chair],
                                  zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])




################  display annotated boxes around chair ###########
aabb = chair.get_axis_aligned_bounding_box()
aabb.color = (0.5,0,0.6)
obb = chair.get_oriented_bounding_box()
obb.color = (0.7,1,0.1)
o3d.visualization.draw_geometries([chair, aabb, obb],
                                  zoom=0.7,
                                  front=[0.5439, -0.2333, -0.8060],
                                  lookat=[2.4615, 2.1331, 1.338],
                                  up=[-0.1781, -0.9708, 0.1608])




##########  downsampling chair dataset #########

print("Downsample the point cloud with a voxel of 0.05")
downpcd = pcd.voxel_down_sample(voxel_size=0.05)
o3d.visualization.draw_geometries([downpcd],
                                  zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])




