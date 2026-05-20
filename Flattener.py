import pymupdf as pdf

def flatten_pdf(input_path, output_path):
    input_file = pdf.open(input_path)
    output_file = pdf.open()

    zoom = 3
    matrix = pdf.Matrix(zoom, zoom)

    for page in input_file:
        pix = page.get_pixmap(matrix=matrix)
        new_page = output_file.new_page(width=page.rect.width, height=page.rect.height)
        new_page.insert_image(new_page.rect, pixmap=pix)

    input_file.close()
    output_file.save(
        output_path,
        garbage=3,
        deflate=True
    )
    output_file.close()