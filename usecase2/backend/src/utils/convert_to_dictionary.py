def convert_to_dictionary(rows):
    headers = rows.pop(0)
    result = []
    
    for row in rows:
        row_dict = dict(zip(headers, row))
        result.append(row_dict)
    
    return result