# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cita(models.Model):
    _name = 'quintopet.cita'
    _description = 'La cita'

    horaInicio = fields.Datetime("Inicio", autodate=False)
    horaFin = fields.Datetime("Fin", autodate=False)
    estado = fields.Char("Estado", size=64, required=False)
    diagnostico = fields.Text("Diagnostico", size=64, required=False)

    mascota_id = fields.Many2one(
        'quintopet.mascota',
        string='Mascota'
    )

    veterinario_id = fields.Many2one(
        'quintopet.veterinario',
        string='Veterinario'
    )

    tratamiento_ids = fields.One2many(
        'quintopet.tratamiento',
        'cita_id',                
        string='Tratamientos'              
    )