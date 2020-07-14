from django.shortcuts import render
refcodes = [
{
    'id': '1',
    'code': '123',
    'system': '4141',
    'operation_number': '6021',
    'operation_name': 'CTLMAYORTEST',
    'hm_description': 'something wrong with the cables',
    'fix_action' : 'Jump around the system five times and scream "Im an Idiot"'
}
]
# Create your views here.
def references_db(request):
    return render(request, 'app-refcodes.html', {'refcodes' : refcodes})
