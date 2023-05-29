# Attributes

## Attributes of widgets

All widgets have some attributes that can be used to customize the widget. The attributes are:

### load_css

This attribute is used to load the CSS of the widget. It is a boolean value. If it is `True`, the CSS of the widget will be loaded. If it is `False`, the CSS of the widget will not be loaded. The default value is `False`. If you need to add the CSS of the widget, you can add it manually. `FormWidget(load_css=True)` will load the CSS of the `FormWidget` widget.

### forms_type

This attribute is used to set the type of the form. It is a string value. The default value is `loginform`. Currently, we are working on `loginform`, `registrationform`, `contactform`, `searchform`, `subscribeform` and `commentform`. More will come soon. `FormWidget(forms_type="loginform")` will set the type of the form to `loginform`.

### action

This attribute is used to set the action of the form. It is a string value. The default value is `#`. `FormWidget(action="/login")` will set the action of the form to `/login`. If you need to set the action of the form to the current page, you can set it to `""` or `#`.

### method

This attribute is used to set the method of the form. It is a string value. The default value is `POST`. `FormWidget(method="GET")` will set the method of the form to `GET`.

### add_element

This attribute is used to add more elements to the form. You can use it `FormWidget().add_element(element)` to add an element to the form. `FormWidget().add_element(Input(type="text", name="username"))` will add an input element to the form.

