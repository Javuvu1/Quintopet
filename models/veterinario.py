# -*- coding: utf-8 -*-

from odoo import models, fields, api


class veterinario(models.Model):
    _inherit="quintopet.persona"
    _name = "quintopet.veterinario"
    
    especialidad = fields.Char("Especialidad", size=64, required=True)
    numeroColegiado = fields.Integer("Numero de colegiado", default=25, required=True, readonly=False)
    
    nomina = fields.Float("Nomina",(5, 2), required=True)