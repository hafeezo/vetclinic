# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vetclinic(models.Model):
    _name = 'vetclinic.animal'
    _description = 'Vetclinic Animal model'

    name = fields.Char('Name', size=32)
    color = fields.Char('Colour', size=6)
    weight = fields.Float('Weight')
    owner = fields.Many2one('res.partner', "Owner")