from PIL import Image , ImageDraw,ImageFont
"""
这是给图片加水印的方式，用循环可以加多个图片
"""
#读取pdf的是按照红绿蓝rgb方式的颜色排列，而png格式图片rgba多个a透明度
image_before=Image.open(r'C:\Users\lihao\Desktop\dify\屏幕截图 2025-09-25 100835.png',)

#转成RGBA格式
rgba_image=image_before.convert('RGBA')

# 水印层
mix_cover=Image.new('RGBA',rgba_image.size,(255,25,25,60))
print(mix_cover)
# 绘制水印层
on_mix=ImageDraw.Draw(mix_cover)

text='@lihao8'
#添加字体，没有可默认
# front=ImageFont.truetype()
font = ImageFont.load_default()
bbox=on_mix.textbbox((0, 0), text,font=font)
text_size_x=bbox[2]-bbox[0]
text_size_y=bbox[3]-bbox[1]

# 设置字体放的位置.这个是右下角，相对的位置，所以用最大来减去
text_xy=(rgba_image.size[0]-text_size_x,rgba_image.size[1]-text_size_y)
#设置字体的透明度和颜色
on_mix.text(text_xy,text,font=font,fill=(255,255,255,100))

#合并起来
image_with_text=Image.alpha_composite(rgba_image,mix_cover)
#保存起来
image_after=image_with_text.convert('RGBA')
image_after.save(r'C:\Users\lihao\Desktop\dify\水印版.png',)
print('success')