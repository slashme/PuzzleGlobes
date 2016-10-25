#From http://blender.stackexchange.com/questions/41351/is-there-a-way-to-select-edges-marked-as-sharp-via-python

import bpy
import bmesh

obj = bpy.context.edit_object
me = obj.data

bm = bmesh.from_edit_mesh(me)
for e in bm.edges:
    if not e.smooth:
        e.select = True

bmesh.update_edit_mesh(me, False)
