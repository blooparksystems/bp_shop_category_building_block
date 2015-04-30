# -*- coding: utf-8 -*-
##############################################################################
#
# Odoo, an open source suite of business apps
# This module copyright (C) 2015 bloopark systems (<http://bloopark.de>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.models import Model
from openerp import fields


class product_public_category(Model):

    """Adds the fields for Building Block."""

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
