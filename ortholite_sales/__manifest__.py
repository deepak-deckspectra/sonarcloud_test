# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Sales Customization",
    'version': '1.0',
    'summary': 'Sales',
    'license': 'LGPL-3',
    'description': """
        Sales Customization - Task ID: 3946632,
        Add a field in the Sales Analysis model for filter and groupby records with tags
    """,

    # auther
    'author': "Odoo PS-IN",
    'website': "http://www.odoo.com",
    'category': "Customizations",

    # any module necessary for this one to work correctly
    'depends': ['sale_management', 'crm_iap_mine', 'website_crm_iap_reveal'],

    #Data
    'data': [
        'security/ir.model.access.csv',
        'report/sale_report_views.xml',
        'views/sales_order_views.xml',
        'views/res_users_views.xml',
        'views/crm_menu_views.xml',
    ],

    'installable': True,
    'application': False,
}
