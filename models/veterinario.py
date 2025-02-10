# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class veterinario(models.Model):
    _inherit="quintopet.persona"
    _name = 'quintopet.veterinario'
    
    especialidad = fields.Char("Especialidad", size=64, required=True)
    numeroColegiado = fields.Integer("Numero de colegiado", required=True, readonly=False)
    nomina = fields.Float("Nomina",(5, 2), required=True)
    foto = fields.Binary("Foto")

    cita_ids = fields.One2many(
        'quintopet.cita',
        'veterinario_id',
        string="Citas",
    )
    
    @api.onchange('nomina')
    def _onchange_nomina(self):
        if self.nomina and self.nomina < 500:
            return {
                'warning': {
                    'title': "Nómina demasiado baja",
                    'message': "La nómina no puede ser menor a 500.",
                }
            }

    @api.constrains('numeroColegiado')
    def _check_numeroColegiado(self):
        for record in self:
            if record.numeroColegiado <= 0:
                raise ValidationError("El número de colegiado debe ser un número positivo.")
    
    @api.constrains('nomina')
    def _check_nomina(self):
        for record in self:
            if record.nomina < 0:
                raise ValidationError("La nómina no puede ser negativa.")


