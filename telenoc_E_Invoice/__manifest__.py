# -*- coding: utf-8 -*-

{
    "name": "e-Invoice KSA | tax invoice | report | qrcode | ZATCA | vat  | electronic | einvoice | e-invoice sa | accounting | tax  | Zakat, Tax and Customs Authority | invoice ",
    "version": "1.2",
    "depends": [
        'base', 'web', 'account',
    ],
    "author": "Telenoc",
    "category": "Accounting",
    "website": "https://www.telenoc.org/",
    "images": [],
    "price": "0",
    "license": "OPL-1",
    "currency": "USD",
    "summary": "e-Invoice in Kingdom of Saudi Arabia KSA | tax invoice | vat  | electronic | e invoice | accounting | tax | free | ksa | sa |Zakat, Tax and Customs Authority | الفاتورة الضريبية | الفوترة  الالكترونية |   هيئة الزكاة والضريبة والجمارك",
    "description": """
    e-Invoice in Kingdom of Saudi Arabia
    and prepare tax invoice to be ready for the second phase.
    Zakat, Tax and Customs Authority
    الفوترة الإلكترونية - الفاتورة الضريبية - المملكة العربية السعودية
    المرحلة الاولي -  مرحلة الاصدار 
    هيئة الزكاة والضريبة والجمارك

    Versions History --------------------
    
     * version 1.2: 10-Oct-2021
         - Initial version compatible with odoo v15 , tax invoice report, QR code

    
    """
    ,
    "data": [
        "view/partner.xml",
        "report/base_document_layout.xml",
        "report/account_move.xml",

    ],
    "installable": True,
    "auto_install": False,
    "application": True,
    'assets': {
        'web.report_assets_common': [
            'tele_e_Invoice/static/css/report_style.css',
        ],
    },
}
