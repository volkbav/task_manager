# функция для добавления атрибутов в класс
def attrs_add(fields, placeholders):
    for name, field in fields.items():
        if name in placeholders:
            field.widget.attrs.update({
                "placeholder": placeholders[name],
                "class": "form-control",
            })
