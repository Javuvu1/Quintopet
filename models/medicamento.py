# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Medicamento(models.Model):
    _name = 'quintopet.medicamento'  
    _description = 'Un medicamento'
    
    nombreMedicamento = fields.Char("Nombre del Medicamento", size=64, required=True)
    referencia = fields.Char("Referencia", size=32, required=True)
    precio = fields.Float("Precio", required=True)  
    prospecto = fields.Binary("Prospecto")
    fechaCaducidad = fields.Date("Fecha de caducidad", default=fields.Date.context_today)

    tratamiento_ids = fields.Many2many(
        'quintopet.tratamiento',  
        'tratamiento_medicamento_rel', 
        'medicamento_id',  
        'tratamiento_id',  
        string='Tratamientos'  
    )
