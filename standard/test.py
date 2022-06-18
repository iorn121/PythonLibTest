def document_it(func):
    def show_info(*args, **kwargs):
        print('function name: ',func.__name__)
        print('args: ',args)
        print('kwargs: ',kwargs)
        result=func(*args, **kwargs)
        print('result: ',result)
    return show_info


class Cat:
    def __init__(self, name):
        self.name =name


cat=Cat('Kuro')
print(cat.name)

@document_it
def sum(a,b):
    return a+b

@document_it
def apply_discount(product,discount):
    price=int(product['price']*(1.0-discount))
    assert 0<= price <=product['price']
    return price

from pprint import pprint
import struct
from turtle import bgcolor
valid_png_header=b'\x89PNG\r\n\x1a\n'
from PIL import Image
screen=(1,1)
bgcolor=(0,0,0)
file_name="black.png"
import os
if not os.path.exists(file_name):
    img=Image.new("RGB",screen,bgcolor)
    img.save(file_name)
    print("create new image")
# import sys
# print(sys.byteorder) # little
import zlib
class Image_Info:
    def __init__(self,file_name):
        valid_png_header=b"\x89PNG\r\n\x1a\n"
        self.f=open(file_name,"rb")
        self.data=self.f.read()
        self.png_head=struct.unpack_from(">8s",self.data,0)
        if self.png_head[0]==valid_png_header:
            self.width=struct.unpack_from(">I",self.data,16)
            self.height=struct.unpack_from(">I",self.data,20)
            self.bit_depth=struct.unpack_from(">B",self.data,24)
            self.color_type=struct.unpack_from(">B",self.data,25)
            self.compression=struct.unpack_from(">B",self.data,26)
            self.filter_method=struct.unpack_from(">B",self.data,27)
            self.interlace=struct.unpack_from(">B",self.data,28)
            self.crc=struct.unpack_from(">I",self.data,29)
            self.length=struct.unpack_from(">I",self.data,33)
            self.ctype=struct.unpack_from(">4s",self.data,37)
            self.idata=struct.unpack_from(">"+str(self.length[0]//2*2)+"B",self.data,41)
            self.idata=zlib.decompress(bytearray(self.idata))
            print("read complete")
        else:
            print("read error")
        self.f.close()
    def write_info(self,file_name):
        self.ff=open(file_name,"w")
        self.ff.write(f"width: {self.width}\n")
        self.ff.write(f"height: {self.height}\n")
        self.ff.write(f"bit_depth: {self.bit_depth}\n")
        self.ff.write(f"color_type: {self.color_type}\n")
        self.ff.write(f"compression: {self.compression}\n")
        self.ff.write(f"filter_method: {self.filter_method}\n")
        self.ff.write(f"interlace: {self.interlace}\n")
        self.ff.write(f"crc: {self.crc}\n")
        self.ff.write(f"length: {self.length}\n")
        self.ff.write(f"ctype: {self.ctype}\n")
        self.ff.write(f"idata: {self.idata}\n")
        self.ff.close()
logo_file="logo.png"
img=Image_Info(logo_file)
img.write_info("logo_info.txt")
# d=open(logo_file,"rb").read()
# pprint(struct.unpack_from(">4s",d,41))
