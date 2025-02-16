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

# Function to convert mesh data to JSON
def mesh_to_json(mesh):
    vertices = [[v.co.x, v.co.y, v.co.z] for v in mesh.vertices]
    faces = [[v for v in f.vertices] for f in mesh.polygons]
    return {"vertices": vertices, "faces": faces}

# Function to convert object to JSON
def object_to_json(obj):
    mesh_data = mesh_to_json(obj.data) if obj.type == 'MESH' else None
    obj_data = {
        "name": obj.name,
        "location": list(obj.location),
        "mesh": mesh_data,
        "children": [object_to_json(child) for child in obj.children]
    }
    return obj_data

# Get the active object and convert it to JSON
obj_data = object_to_json(bpy.context.view_layer.objects.active)

# Write the JSON data to a file
with open(output_json_path, 'w') as json_file:
    json.dump(obj_data, json_file, indent=4)

print(f"Exported {obj.name} to {output_json_path}")