import unittest
from fronty import html


class TestElements(unittest.TestCase):
    '''Test the BaseElement class.'''

    def test_base_element(self):
        '''
        Test the BaseElement class.
        This is the base class for all elements. It is used to create new elements. 
        '''
        self.assertEqual(

            # Test case
            html.BaseElement(
                'tag',
            )
            .attr('name', 'value')
            .id('id')
            .class_('class1 class2 classNth')
            .style(color='red', background='blue')
            .render(),

            # Expected result
            '<tag name="value" id="id" class="class1 class2 classNth" style="color:red;background:blue;"></tag>'
        )

    def test_empty_element(self):
        '''Test the Empty element.'''
        self.assertEqual(
            html.Empty().render(),
            ''
        )

    def test_website_elements(self):
        '''Test the website elements.'''
        self.assertEqual(
            html.Html(
                html.Head(
                    html.Meta(charset="utf-8"),
                    html.Title("Test case"),
                ),
                html.Body(
                    html.Div(
                        html.Text(
                            'This is a paragraph.'
                        )
                    ).class_('container'),

                    html.Footer(
                        html.Text(
                            'This is a footer.'
                        )
                    ).id('footer')
                ),
            ).render(),

            '<!DOCTYPE html><html><head><meta charset="utf-8"><title>Test case</title></head><body><div class="container"><p>This is a paragraph.</p></div><footer id="footer"><p>This is a footer.</p></footer></body></html>'
        )

    
    def test_attr_counts(self):
        '''Test the attr counts method.'''

        # Test case
        self.assertEqual(
            html.Div(
                html.Input()
                .attr('type', 'text')
                .attr('name', 'InputElement')
                .attr('value', 'InputValue')
                .attr('placeholder', 'InputPlaceholder')
                .attr('required', True)
                .attr('disabled', False)
                .attr('readonly', False)
                ,
            ),

            # Expected result
            '<div><input type="text" name="InputElement" value="InputValue" placeholder="InputPlaceholder" required="True" disable="False" readonly="False"></div>'
        )


if __name__ == '__main__':
    unittest.main()
