# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from datetime import timedelta
from datetime import datetime

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

    @api.onchange('horaInicio')
    def _onchange_horaInicio(self):
        if self.horaInicio:
            self.horaFin = self.horaInicio + timedelta(hours=1)

    @api.constrains('horaInicio', 'horaFin')
    def _check_datetime_order(self):
        for record in self:
            if record.horaInicio and record.horaFin:
                if record.horaFin <= record.horaInicio:
                    raise ValidationError(
                        "La fecha y hora de fin deben ser mayores que la fecha y hora de inicio."
                    )
                
    def btn_BorrarCita(self):
        if self.horaFin and self.horaFin < datetime.now():
            self.unlink()  
        else:
            raise UserError('No se puede eliminar una cita que no ha acabado')
    