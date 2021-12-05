# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Telenoc K.S.A - Invoice',
    'version': '1.0.0',
    'author': 'Odoo Team, Telenoc',
    'category': 'Accounting/Localizations',
    'license': 'LGPL-3',
    'description': """
    Invoices for the Kingdom of Saudi Arabia
""",
    'depends': ['l10n_sa', 'telenoc_e_invoice'],
    'data': [
        'views/view_move_form.xml',
        'views/report_invoice.xml',
    ],
}
