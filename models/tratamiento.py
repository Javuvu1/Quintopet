# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Tratamiento(models.Model):
    _name = 'quintopet.tratamiento'
    _description = 'Un tratamiento'

    nombreMedicamento = fields.Char("Nombre del Medicamento", size=64, required=True)
    descripcion = fields.Text("Descripción", size=200, required=True)
    patologia = fields.Char("Patología", size=64, required=True)
    inicioTratamiento = fields.Date("Inicio Tratamiento", default=fields.Date.context_today)
    finTratamiento = fields.Date("Fin Tratamiento", default=fields.Date.context_today)

    cita_id = fields.Many2one(
        'quintopet.cita',                 
        string='Citas'                    
    )

    medicamento_ids = fields.Many2many(
        'quintopet.medicamento',  
        'tratamiento_medicamento_rel', 
        'tratamiento_id',  
        'medicamento_id', 
        string='Medicamentos'  
    )   
    
