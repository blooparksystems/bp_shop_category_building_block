# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013-Today OpenERP SA (<http://www.openerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Building Block for Shop Category",

    'summary': """
        enables Building Blocks for Shop Category in the odoo ecommerce shop frontend""",

    'description': """
         enables Building Blocks for Shop Category in the odoo ecommerce shop frontend""",

    'author': "bloopark systems GmbH & Co. KG",
    'website': "http://www.bloopark.de",

    'category': 'shop',
    'version': '1.0',

    'depends': [
        'base',
        'website_sale'
    ],
    'data': [
        'views/templates.xml',
    ],

    'demo': [
    ],

    'tests': [
    ],
}