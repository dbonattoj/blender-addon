############################################################################
#  This file is part of the 4D Light Field Benchmark.                      #
#                                                                          #
#  This work is licensed under the Creative Commons                        #
#  Attribution-NonCommercial-ShareAlike 4.0 International License.         #
#  To view a copy of this license,                                         #
#  visit http://creativecommons.org/licenses/by-nc-sa/4.0/.                #
#                                                                          #
#  Authors: Katrin Honauer & Ole Johannsen                                 #
#  Contact: contact@lightfield-analysis.net                                #
#  Website: www.lightfield-analysis.net                                    #
#                                                                          #
#  This add-on is based upon work of Maximilian Diebold                    #
#                                                                          #
#  The 4D Light Field Benchmark was jointly created by the University of   #
#  Konstanz and the HCI at Heidelberg University. If you use any part of   #
#  the benchmark, please cite our paper "A dataset and evaluation          #
#  methodology for depth estimation on 4D light fields". Thanks!           #
#                                                                          #
#  @inproceedings{honauer2016benchmark,                                    #
#    title={A dataset and evaluation methodology for depth estimation on   #
#           4D light fields},                                              #
#    author={Honauer, Katrin and Johannsen, Ole and Kondermann, Daniel     #
#            and Goldluecke, Bastian},                                     #
#    booktitle={Asian Conference on Computer Vision},                      #
#    year={2016},                                                          #
#    organization={Springer}                                               #
#    }                                                                     #
#                                                                          #
############################################################################

bl_info = {
    'name': 'Light Field Renderer',
    'author': 'Ole Johannsen, Katrin Honauer, Daniele Bonatto (2.8 port)',
    'description': 'Scripts to create a static light field setup',
    'version': (1, 0, 0),
    'blender': (2, 80, 0),
    #'api': 36103,
    'location': 'View3D > Tool Shelf > 4D Light Field Renderer',
    'url': 'https://www.informatik.uni-konstanz.de/cvia/',
    'category': 'Render'
}

if "bpy" in locals():
    import imp 
    imp.reload(gui)
    imp.reload(lightfield_simulator)
    imp.reload(updates)
    imp.reload(import_export)
    imp.reload(LFProperty)
else:
    from . import gui, lightfield_simulator, updates, import_export, LFProperty
    
import bpy



classes = ( import_export.OBJECT_OT_save_lightfield,
            import_export.OBJECT_OT_load_lightfield,
            lightfield_simulator.OBJECT_OT_show_frustum,
            lightfield_simulator.OBJECT_OT_hide_frustum,
            lightfield_simulator.OBJECT_OT_update_lightfield,
            lightfield_simulator.OBJECT_OT_create_lightfield,
            lightfield_simulator.OBJECT_OT_delete_lightfield,
            lightfield_simulator.OBJECT_OT_render_lightfield,
            gui.VIEW3D_PT_lightfield_setup,
            LFProperty.LFPropertyGroup,
)

#register, unregister = bpy.utils.register_classes_factory(classes)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.LF = bpy.props.PointerProperty(type=LFProperty.LFPropertyGroup)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.LF

"""
def register():
    # register properties
    bpy.utils.register_class(LFPropertyGroup)
    bpy.types.Scene.LF = bpy.props.PointerProperty(type=LFPropertyGroup)
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)
"""

if __name__ == "__main__":
    register()
