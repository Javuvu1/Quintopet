# -*- coding: utf-8 -*-

from odoo import models, fields, api


class prueba_medica(models.Model):
    _name = 'quintopet.prueba_medica'
    
    fechaHoras = fields.Datetime("Fecha y Hora", required=True)
    tipoPrueba = fields.Char("Tipo de prueba", size=100, required=True)
    observaciones= fields.Text("Observaciones", size=255, required= False)
    