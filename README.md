Blender **2.8** addon to configure and render light fields with depth and disparity maps.

Please don't hesitate to contact the original authors for any kind of questions, feedback, wishes, or bug reports.

# **REMARKS**

The original authors [blender-addon](https://github.com/lightfield-analysis/blender-addon) created this addon for Blender 2.79.
However, recently, Blender 2.8 came out and became the new standard for 3D rendering with its fast rendering engine Eevee.

I tried to do my best to port the addon to Blender 2.8 in a **very short** amount of time.

I'm far from an expert in Blender, and even less in Blender scripting.

If someone find bugs, feel free to fill issues and send patches :)

I navigated through several forks of the main repository and integrated here some features that I found interesting.


## Eevee vs Cycles for Depth Maps

If you write your own renderer, it will appear normally in the list :)

Cycles seems to have a **bug** rendering depth maps:

- Eevee: depth is the distance with the camera axis.
- Cycles: depth is the distance between the camera and the object.

To render "accurate" depthmaps, use Eevee.

# Installation

Please clone the git repository into the blender/VERSION/scripts/addons/ folder of your local blender installation.
Afterwards, you can activate the add-on at File -> User Preferences -> Add-ons -> Render.
Once activated, the add-on can be found in the tool menu ('n' shortcut)


# Usage


<img src="http://lightfield-analysis.net/benchmark/github_readme/blender_screenshot.png" width=300 align="right"/>

You can generate a new camera grid using the 'Add Camera Grid' button. Any changes to the parameters of the camera grid will be updated instantaneously. For better visualization, we added a frustum that shows the volume that is covered by the light field for a given disparity range. As described in the additional material of our paper, the camera grid is focused on a certain plane. 

Please note, the cameras are shifted, not rotated, so the optical axes are still parallel! If you want to generate a camera grid which is focused at infinity, i.e. has non-shifted identical cameras, you can set the focus distance to 0.

To render the scene, press the 'Render Light Field' button. It will render all views to the given directory using the renderer and the render settings you have chosen. For depth/disparity map generation the add-on switches to the internal blender renderer. There are two reasons for this behavior. First, it is much faster than the e.g. cycles renderer and better suited to generate high resolution depth maps. Second, different renderer have different interpretations of depth. The internal renderer computes the distance in Z direction, while cycles computes the Euclidean distance. To bypass knowing all potential renderer we fall back to the ubiquitous blender renderer.



# License
This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. 
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/. 
 
Original authors: Katrin Honauer & Ole Johannsen 
Blender 2.8 port: Daniele Bonatto

Website: www.lightfield-analysis.net 

 
This add-on is based upon work of Maximilian Diebold. 

The 4D Light Field Benchmark was jointly created by the University of Konstanz and the HCI at Heidelberg University. If you use any part of the benchmark, please cite our paper "A dataset and evaluation methodology for depth estimation on 4D light fields". Thanks! 
 
 @inproceedings{honauer2016benchmark, 
 title={A dataset and evaluation methodology for depth estimation on 
 4D light fields}, 
 author={Honauer, Katrin and Johannsen, Ole and Kondermann, Daniel 
 and Goldluecke, Bastian}, 
 booktitle={Asian Conference on Computer Vision}, 
 year={2016}, 
 organization={Springer} 
 } 
 
