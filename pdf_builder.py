from fpdf import FPDF

def add_footer(pdf, text, page_n, total_pages):
    # Arial italic 8
    pdf.set_font('Arial', 'I', 8)
    # Page number
    pdf.text(10, 292, '%s %d/%d'%(text, page_n ,total_pages))

card_w = 63
card_h = 88
margin = 0.2
border = 10

def build_pdf_with_cards(footer_text, card_images):
    pdf = FPDF('P', 'mm', 'A4')
    num = len(card_images)
    pages = num // 9 + 1
    for page_i in range(pages):
        pdf.add_page()
        image_batch = card_images[page_i * 9: page_i * 9 + 9]
        for i, image in enumerate(image_batch):
            x_i = i % 3
            y_i = i // 3
            pdf.image(
                image,
                x = (margin + card_w) * x_i + border, 
                y = (margin + card_h) * y_i + border,
                w = card_w,
                h = card_h,
                type = '', link = '')
        add_footer(pdf, footer_text, page_i + 1, pages)
    return pdf
