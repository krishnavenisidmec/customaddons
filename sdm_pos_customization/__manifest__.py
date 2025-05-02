{
    'name': 'sdm_customization',
    'version': '18.0',
    'category': 'Point of Sale',
    'description': """
        This module brings the technical requirement for the Argentinean regulation.
        Install this if you are using the Point of Sale app in Argentina.
            """,
    'depends': [
        'base','point_of_sale',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'sdm_pos_customization/static/src/js/product.js',
            'sdm_pos_customization/static/src/xml/product_card.xml',
            'sdm_pos_customization/static/src/xml/product_screen.xml',
            'sdm_pos_customization/static/src/js/orderline.js',
            'sdm_pos_customization/static/src/xml/orderline.xml',
            'sdm_pos_customization/static/src/xml/orderwidget.xml',

        ],

    },


}
