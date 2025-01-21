import bpy
import json

# Set the output file path for OBJ
output_obj_path = "put your path/output.obj"

# Select the active object
obj = bpy.context.active_object

# Ensure the object is selected
bpy.ops.object.select_all(action='DESELECT')
obj.select_set(True)

# Export the selected object to an OBJ file using wm.obj_export
bpy.ops.wm.obj_export(filepath=output_obj_path)

# Set the output file path for JSON
output_json_path = "put your path/output.json"

# Convert the object to JSON
obj_data = {
    "name": obj.name,
    "vertices": [v.co.to_tuple() for v in obj.data.vertices],
    "edges": [e.vertices[:] for e in obj.data.edges],
    "faces": [f.vertices[:] for f in obj.data.polygons]
}

# Write the JSON data to a file
with open(output_json_path, 'w') as f:
    json.dump(obj_data, f, indent=4)

print(f"Exported {obj.name} to {output_json_path}")