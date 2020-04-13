from fpdf import FPDF
import pandas as pd
import numpy as np
from do_statistics import reportYear

def create_pdf(variable, value, spacing=1):
    # Generate FPDF object and add page
    # FPDF(orientation, unit, format)
    pdf = FPDF("P","mm","A4")
    pdf.add_page()

    # fpdf.set_font(family, style = '', size = 0)
    # Before writing text
    pdf.set_font("Arial", "B", 24)
    #Title
    pdf.cell(200, 10, txt="California Wilfires [2013-2019]", ln=1, align="C")
    pdf.ln()

    # Table section
    pdf.set_font("Courier", "B", 16)
    if variable == 'Year':
        pdf.cell(200, 10, txt="Number of fires by year", ln=1, align="L")
    if variable == 'HaBurned':
        pdf.cell(200, 10, txt="Burned area in ha by year", ln=1, align="L")
        
    df = reportYear(variable, value)
    # round decimals and convert numbers to strings
    data = (df.round(2)).applymap(str)
    data
    # Create a list to iterate
    data_list = [data.columns.values.tolist()] + data.values.tolist()
   
    # Print the table
    pdf.set_font("Arial", size=12)
    col_width = pdf.w / 4.5
    row_height = pdf.font_size
    for row in data_list:
        for item in row:
            pdf.cell(col_width, row_height*spacing,
                     txt=item, border=1, align= "C")
        pdf.ln(row_height*spacing)

    # Plot section
    pdf.set_font("Courier", "B", 16)
    pdf.ln()
    if variable == 'Year':
        pdf.cell(200, 10, txt="Evolution of wildfires number", ln=1, align="L")
        pdf.image("../output/nfires.png", x = 35, y = None, w = 140, h = 100)
    if variable == 'HaBurned':
        pdf.cell(200, 10, txt="Total of burned area by year", ln=1, align="L")
        pdf.image("../output/burnedArea.png", x = 35, y = None, w = 140, h = 100)
    
    pdf.output('../output/'+variable+'_report.pdf')
    
#if __name__ == '__main__':    
 #   create_pdf('Year','count', spacing=1)

    
