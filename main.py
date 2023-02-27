from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="p", unit="mm", format="a4")
fs = pd.read_csv("topics.csv")

for index, row in fs.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", size=20, style="I")
    pdf.set_text_color(100, 20, 50)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="l", ln=1)
    pdf.line(10, 22, 200, 22)

pdf.output("output.pdf")
