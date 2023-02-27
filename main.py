from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="p", unit="mm", format="a4")
pdf.set_auto_page_break(auto=False, margin=0)
fs = pd.read_csv("topics.csv")


def set_footer(line):
    pdf.ln(line)
    pdf.set_font(family="Times", size=10, style="BI")
    pdf.line(10, 288, 200, 288)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)


for index, row in fs.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", size=20, style="I")
    pdf.set_text_color(100, 20, 50)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="l", ln=1)
    pdf.line(10, 22, 200, 22)
    # set footer
    set_footer(265)

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        set_footer(277)

pdf.output("output.pdf")
