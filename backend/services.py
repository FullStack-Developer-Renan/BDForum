import csv

FIELDNAMES = ['message_content', 'user_type']

class CallService():
    def read_data(filename):
        try:
            current_file = open(filename)
            try:
                reader = csv.DictReader(current_file)
                data = list(reader)
                current_file.close()
                return data
            except ValueError:
                return []
        except FileNotFoundError:
            new_file = open(filename, 'w+')
            new_file.writelines(u'')
            new_file.close
            return []
    
    def post_message(filename, **kwargs):
        data_original = CallService.read_data(filename)      
        new_file = open(filename, 'w+')
        writer = csv.DictWriter(new_file, fieldnames=FIELDNAMES)
        data_original.append(kwargs)
        writer.writeheader()
        writer.writerows(data_original)
        new_file.close()
        return kwargs
        
