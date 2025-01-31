# -*- coding: utf-8 -*-
{
    'name': "quintopet",

    'summary': """
        Esta es una aplicación para gestionar clínicas veterinarias""",

    'description': """
        Esta es una aplicación para gestionar clínicas veterinarias
    """,

    'author': "Oscar Barrera, Javier Castillo, Adrián Juan, Jose Francisco Mora",
    'website': "http://www.quintopet.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    
    'application' : True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/cliente_view.xml',
        'views/veterinario_view.xml',
        'views/mascota_view.xml',
        'views/cita_view.xml',
        'views/tratamiento_view.xml',
        'views/medicamento_view.xml',
        'views/menu_view.xml',
        'views/prueba_medica.xml',
        'views/clinica.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
