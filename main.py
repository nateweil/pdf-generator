from fpdf import FPDF
import pandas as pandas


data = pandas.read_csv("topics.csv")

pdf = FPDF(orientation="portrait", unit="mm", format="letter")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in data.iterrows():
    # Just three variable assignments, stacked together for fun.
    order, topic, pages = row["Order"], row["Topic"], row["Pages"]

    # I initially used "while i < pages" and incremented i, but this loop is neater.
    for i in range(pages):
        pdf.add_page()

        if i == 0:
            # Add the header to just the first page of each topic
            pdf.set_font(family="Times", style="B", size=24)
            pdf.set_text_color(175, 0, 0)
            pdf.cell(w=0, h=12, txt=topic, align="L", ln=1)
            pdf.line(x1=11, y1=21, x2=200, y2=21)

            # pdf.ln adds break lines
            pdf.ln(240)
        else: # If it's a blank page, needs more break lines
            pdf.ln(251)

        pdf.set_font(family="Times", style="i", size=10)
        pdf.set_text_color(150,150,150)
        pdf.cell(w=0, h=10, txt=f"{topic} {str(i+1)}", align="R")

pdf.output("output.pdf")





"""
pdf.add_page()

pdf.set_font(family="Arial", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello there!", align="L", ln=1, border=1)

pdf.set_font(family="Times", style="i", size=12)
pdf.cell(w=0, h=12, txt="Second line", align="R", ln=1, border=1)

pdf.output("output.pdf")
"""