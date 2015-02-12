 # -*- coding: utf-8 -*-
from openerp.models import Model
from openerp import fields

class product_public_category(Model):
    _inherit = 'product.public.category'

    # Fields for the different Block injections
    website_description_1 = fields.Html(
        string='Description 1 for the website',
        translate=True
    )
    website_description_2 = fields.Html(
        string='Description 2 for the website',
        translate=True
    )
    website_description_3 = fields.Html(
        string='Description 3 for the website',
        translate=True
    )