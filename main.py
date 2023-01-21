from fpdf import FPDF
import pandas as pandas


data = pandas.read_csv("topics.csv")

pdf = FPDF(orientation="portrait", unit="mm", format="letter")

for index, row in data.iterrows():
    order, topic, pages = row["Order"], row["Topic"], row["Pages"]

    i=0
    while i < pages:
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(175, 0, 0)
        pdf.cell(w=0, h=12, txt=topic, align="L", ln=1)
        pdf.line(x1=11, y1=21, x2=200, y2=21)
        i+=1


pdf.output("output.pdf")





"""
pdf.add_page()

pdf.set_font(family="Arial", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello there!", align="L", ln=1, border=1)

pdf.set_font(family="Times", style="i", size=12)
pdf.cell(w=0, h=12, txt="Second line", align="R", ln=1, border=1)

pdf.output("output.pdf")
"""