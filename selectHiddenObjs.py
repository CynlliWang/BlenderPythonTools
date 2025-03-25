import bpy

# 手动取消隐藏所有物体（不依赖 bpy.ops）
for obj in bpy.context.view_layer.objects:
    obj.hide_set(False)      # 取消隐藏
    obj.hide_select = False  # 允许选择

# 选中所有 Mesh 物体
selected_objs = []
for obj in bpy.context.view_layer.objects:
    if obj.type == 'MESH':
        obj.select_set(True)
        selected_objs.append(obj)

# 打印结果
print(f"选中 {len(selected_objs)} 个物体")
