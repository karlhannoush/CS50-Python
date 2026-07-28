from fpdf import FPDF,Align

name = input("What's your name? ")

pdf = FPDF()
pdf.add_page() 
pdf.image("shirtificate.png",x=Align.C,y=80,w=180)
pdf.set_font('Helvetica', style='B', size=32)
pdf.cell(0,30, txt='CS50 Shirtificate', border=0, ln=1, align='C',)
pdf.set_text_color(255, 255, 255)
pdf.cell(0,210,txt=f"{name} took CS50", border=0, ln=1, align='C')
pdf.output("shirtificate.pdf")    
    