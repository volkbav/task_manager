# функция для добавления атрибутов в класс
def attrs_add(fields, placeholders):
    
    for name, field in fields.items():
        field.widget.attrs.setdefault('class', 'form-control')
        if name in placeholders:
            field.widget.attrs['placeholder'] = placeholders[name]
