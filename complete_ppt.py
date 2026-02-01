from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)
pc = RGBColor(26, 35, 126)
ac = RGBColor(220, 53, 69)
tc = RGBColor(33, 37, 41)
lb = RGBColor(248, 249, 250)
wc = RGBColor(255, 255, 255)
print('Starting PPT creation...')
prs.save('Guowen_Huitong_BP.pptx')
print('Done!')
