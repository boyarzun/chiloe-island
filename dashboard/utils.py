class FormToJsonResponse:
    def __init__(self, *args):
        self.forms = args
        self.response = {}

    def is_valid(self):

        valid_forms = 0
        response = {}
        errors = {}
        
        for form in self.forms:
            if form.is_valid():
                valid_forms += 1
                response = {**response, **form.cleaned_data}
            else:
                errors = {**errors, **form.errors.get_json_data()}
            
        if valid_forms == len(self.forms):
            self.response['ok'] = True
            self.response['form'] = response
            return True
        else:
            self.response['ok'] = False
            self.response['errors'] = errors
            return False

class DataTable:
    def __init__(self, request):
        self.search = request.GET.get('search[value]')
        self.start = str(int(request.GET.get('start')) + 1)
        self.draw = request.GET.get('draw')
        self.data = request.GET.get('columns[0][data]')
        self.name = request.GET.get('columns[0][name]')
        self.searchable = request.GET.get('columns[0][searchable]')
        self.orderable = request.GET.get('columns[0][orderable]')
        self.search_value = request.GET.get('columns[0][search][value]')
        self.search_regex = request.GET.get('columns[0][search][regex]')
        self.data = request.GET.get('columns[1][data]')
        self.name = request.GET.get('columns[1][name]')
        self.searchable = request.GET.get('columns[1][searchable]')
        self.orderable = request.GET.get('columns[1][orderable]')
        self.search_value = request.GET.get('columns[1][search][value]')
        self.search_regex = request.GET.get('columns[1][search][regex]')
        self.data = request.GET.get('columns[2][data]')
        self.name = request.GET.get('columns[2][name]')
        self.searchable = request.GET.get('columns[2][searchable]')
        self.orderable = request.GET.get('columns[2][orderable]')
        self.search_value = request.GET.get('columns[2][search][value]')
        self.search_regex = request.GET.get('columns[2][search][regex]')
        self.data = request.GET.get('columns[3][data]')
        self.name = request.GET.get('columns[3][name]')
        self.searchable = request.GET.get('columns[3][searchable]')
        self.orderable =  request.GET.get('columns[3][orderable] ')
        self.search_value = request.GET.get('columns[3][search][value]')
        self.search_regex = request.GET.get('columns[3][search][regex]')
        self.data = request.GET.get('columns[4][data]')
        self.name = request.GET.get('columns[4][name]')
        self.searchable = request.GET.get('columns[4][searchable]')
        self.orderable = request.GET.get('columns[4][orderable]')
        self.search_value = request.GET.get('columns[4][search][value]')
        self.search_regex = request.GET.get('columns[4][search][regex]')
        self.order_column = request.GET.get('order[0][column]')
        self.order_dir = request.GET.get('order[0][dir]')
        self.length = request.GET.get('length')
        self.search_regex = request.GET.get('search[regex]')