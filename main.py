from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    # sets the header and footer for master page only
    # sets the font to Times, style as Bold and size to 12
    pdf.set_font(family="Times", style="B", size=12)
    # sets the text color to black
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)

    # sets the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=10)
    # Sets the text color to grey
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # sets the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=10)
        # Sets the text color to grey
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

pdf.output("output.pdf")
