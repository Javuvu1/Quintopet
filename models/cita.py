# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cita(models.Model):
    _name = 'quintopet.cita' # modulo.modelo
    _description = 'La cita'
    
    horaInicio = fields.Datetime("Inicio", autodate = False)
    horaFin = fields.Datetime("Fin", autodate = False)
    estado = fields.Char("Estado", size=64, required=False)
    diagnostico = fields.Text("Diagnostico", size=64, required=False)

    mascota_id = fields.Many2one(
        'quintopet.mascota',
        string='Mascota',
        required=False
        )
    