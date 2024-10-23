# -*- coding: utf-8 -*-

from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    is_change_unit_price_so = fields.Boolean(string="Allow User to Change Unit Price")



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_change_unit_price = fields.Boolean(
        string='Not Readonly Unit Price',
        default=lambda self: self.env.user.is_change_unit_price_so,
        compute='_compute_is_change_unit_price')

    def _compute_is_change_unit_price(self):
        for rec in self:
        rec.is_change_unit_price = self.env.user.is_change_unit_price_so