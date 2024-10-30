import bpy

# 遍历选中的对象
for obj in bpy.context.selected_objects:
    # 确保对象是可修改的
    if obj.type == 'MESH':
        # 添加 Subdivision Surface 修改器
        subdiv = obj.modifiers.new(name="Subdivision", type='SUBSURF')
        subdiv.levels = 5
        
        # 添加 Displace 修改器
        displace = obj.modifiers.new(name="Displace", type='DISPLACE')
        
        # 创建 Voronoi 纹理
        texture = bpy.data.textures.new(name="VoronoiTexture", type='VORONOI')
        
        # 将纹理分配给 Displace 修改器
        displace.texture = texture
        
        # 设置 Displace 的纹理坐标
        displace.texture_coords = 'UV'
        
        # 添加 Decimate 修改器
        decimate_0_2 = obj.modifiers.new(name="Decimate_0.2", type='DECIMATE')
        decimate_0_2.ratio = 0.2
        
        # 添加另一个 Decimate 修改器
        decimate_0_5 = obj.modifiers.new(name="Decimate_0.5", type='DECIMATE')
        decimate_0_5.ratio = 0.5

print("修改器已成功添加！")
