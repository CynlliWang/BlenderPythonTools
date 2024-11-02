import bpy

# 获取所有选中的对象
selected_objs = bpy.context.selected_objects
# 检查并确保最后选中的对象是立方体
cube_template = bpy.context.active_object
if cube_template is None or cube_template.type != 'MESH':
    raise ValueError("请确保最后选中的对象是一个立方体")

# 遍历选中的曲线对象，跳过蓝本立方体
for obj in selected_objs:
    if obj == cube_template:
        continue  # 跳过蓝本立方体

    if obj.type == 'CURVE':
        # 创建立方体的实例化副本，所有副本将自动与蓝本同步
        cube_instance = cube_template.copy()
        cube_instance.data = cube_template.data  # 共享蓝本立方体数据
        bpy.context.collection.objects.link(cube_instance)  # 将副本添加到场景中

        # 设置位置为曲线的位置
        cube_instance.location = obj.location

        # 添加Curve修改器并设置目标曲线
        curve_mod = cube_instance.modifiers.new(name="CurveModifier", type='CURVE')
        curve_mod.object = obj  # 设置修改器的目标曲线

print("完成：每个曲线对象上都生成了一个实例化的立方体，并将自动跟随蓝本的修改")
