# Attributes of Component Elements

## Attributes

The attributes of the component elements are the same as the attributes of the html elements. You can use the attributes of the html elements in the component elements. Check the [attributes](https://www.w3schools.com/tags/ref_attributes.asp) of the html elements.

## Important attributes

### id

The `id` attribute is used to give a unique id to a component element. You can use this id to select the component element using JavaScript. `Element().id('something')` or `Element(id='something')` can be used to set the id of a component element.

### class

The `class` attribute is used to give multiple classes to a component element. You can use the same method again to override the previous class. `Element().class_('something1 something2 somethingNth')` or `Element(class='something1 something2 somethingNth')` can be used to set the class of a component element. You can also use `class_` instead of `class` to set the class of a component element as `class` is a reserved keyword in Python and every programming language.

### placeholder

The `placeholder` attribute is used to set the placeholder of a field. `Element().placeholder('something')` or `Element(placeholder='something')` can be used to set the placeholder of a field. It is a method in the `BaseElement` class. You can use this any element that accepts the `placeholder` attribute as it is defined in the `BaseElement` class.

### type

The `type` attribute is used to set the type of a field. `Element().type('something')` or `Element(type='something')` can be used to set the type of a field. It is a method in the `BaseElement` class. You can use this any element that accepts the `type` attribute as it is defined in the `BaseElement` class.

### name

The `name` attribute is used to set the name of a field. `Element().name('something')` or `Element(name='something')` can be used to set the name of a field. It is a method in the `BaseElement` class. You can use this any element that accepts the `name` attribute as it is defined in the `BaseElement` class.

### style

The `style` attribute is used to give inline CSS to a component element. You can use the same method again to override the previous style. `Element().style(color='red', background_color='blue')` can be used to set the style of a component element. This method takes keyword arguments as the CSS properties and their values. Some CSS properties have hyphen in their name. You can use underscore instead of hyphen in the name of the CSS properties. For example, `background-color` can be written as `background_color`.

### attr

The `attr` attribute is used to give attributes to a component element. You can add as much as you need attributes to a component element. `Element().attr('key', 'value').attr('more', 'more')` can be used to set the attribute of a component element. This method takes two arguments as the key and value of the attribute.

### required

The `required` attribute is used to make a input field required. `Element().required` can be used to make a input field required. It is just a property of the `Input` component element. You can use this any element that accepts the `required` attribute as it is defined in the `BaseElement` class.

### disabled

The `disabled` attribute is used to make a input field disabled. `Element().disabled` can be used to make a input field disabled. It is just a property of the `Input` component element. You can use this any element that accepts the `disabled` attribute as it is defined in the `BaseElement` class.

### readonly

The `readonly` attribute is used to make a input field readonly. `Element().readonly` can be used to make a input field readonly. It is just a property of the `Input` component element. You can use this any element that accepts the `readonly` attribute as it is defined in the `BaseElement` class.

### value

The `value` attribute is used to set the value of a field. `Element().value('something')` or `Element(value='something')` can be used to set the value of a field. It is a method in the `BaseElement` class. You can use this any element that accepts the `value` attribute as it is defined in the `BaseElement` class.
