from PIL import Image, ImageDraw, ImageFont
import webbrowser
from datetime import date

input_file = 'template.png'
artwork_file = 'art.png'
output_file = 'temp.pdf'


class Template:
    """Class for the template, containing specific job info"""
    def __init__(self, filename):
        self.object = Image.open(filename).convert("RGB")
        self.height = self.object.height
        self.width = self.object.width
        self.resolution = self.width / 11.5
        self.date = date.today()
        self.day = self.date.day
        self.month = self.date.month
        self.year = self.date.year
        self.filename = filename

    def get_upper_information(self):
        """Get user input for Proof information"""
        info = []
        info.append(str(input("Client Name: ")or 'Client Name'))
        info.append(str(input("Product Name: ")or 'Product Name'))
        info.append(str(input("Product Height: ")or 'Height'))
        info.append(str(input("Product Width: ")or 'Width'))
        info.append(str(input("Quantity: ")or 'Quantity'))
        info.append(str(input("Prints(0/0): ")or '0/0'))
        info.append(str(input("Colors: ")or 'Colors'))
        return info

    def draw_template(self):
        content = self.get_upper_information()
        top_line = '{}/{}/{}   {} / {}'.format(str(self.month),str(self.day),str(self.year)[2:],content[0],content[1])
        bottom_line = 'Final Size {}x{} ({}) - Qty: {} - Prints {} Color: {}'.format(content[2],content[3],'200%',content[4],content[5],content[6])
        fnt = ImageFont.truetype('arial.ttf',30)
        d = ImageDraw.Draw(self.object)

        d.text((600,125), top_line, font=fnt, fill=(0,0,0))
        d.text((600,175), bottom_line, font=fnt, fill=(0,0,0))
        # d.rectangle([self.resolution * 1.5,self.resolution*2,self.resolution*9.5,self.resolution*7],(0,100,0))
        d.rectangle((0,0,self.width-5,self.height-5),outline = (0,0,0))
        return self.object


art = 'rpcat.jpg'


def get_artwork(filepath):
    return Image.open(filepath).convert('RGB')

size = 1600,1000

artwrk = get_artwork(art)

if artwrk.size[1] > size[1]:
    artwrk.thumbnail(size)


print(artwrk.size)
temp = Template('template.png').draw_template()

middle = (int((temp.width - artwrk.width)/2),int((temp.height-artwrk.height)/2))

temp.paste(artwrk,middle)

D = ImageDraw.Draw(temp)


prooffnt = ImageFont.truetype('arial.ttf',400)
D.text((500,500),'PROOF',(25,25,25,25),font = prooffnt)

temp.show()