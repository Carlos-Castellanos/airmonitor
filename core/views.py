import csv

from django.http import HttpResponse
from import_export import resources
from core.models import Author

def export_csv(request):


    # Import-Export library
    author_resource = resources.modelresource_factory(model=Author)()
    dataset = author_resource.export()
    response = HttpResponse(dataset.xls, content_type='text/xls')
    response['Content-Disposition'] = 'atachment; filename="author_library.xls"'
    return response



def import_csv(request):

    # Import-Export library

    with open("ejemplo.csv", "r") as csv_file:
        import tablib

        author_resource = resources.modelresource_factory(model=Author)()
        dataset = tablib.Dataset(headers=[field.name for field in Author._meta.fields]).load(csv_file)
        result = author_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
            author_resource.import_data(dataset, dry_run=False)
        return HttpResponse(
            "Successfully imported"
        )