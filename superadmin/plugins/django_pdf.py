from django.shortcuts import render
from django.http import HttpResponse
from weasyprint import HTML

def generate_pdf(request, template_name='', template_path='', context={}):
    import datetime as dt
    current_datetime = dt.datetime.now()
    # Format the datetime as a string
    formatted_date = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    # Render the HTML template
    html_template = template_path
    # context = {}  # Add any context data you want to pass to the template
    rendered_html = render(request, html_template, context)
    # Create a PDF file
    pdf_file = HTML(string=rendered_html.content).write_pdf()
    # Create a Django response with the PDF content
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'filename="{formatted_date}_{template_name}.pdf"'
    return response