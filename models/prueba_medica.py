from odoo import models, fields, api

class prueba_medica(models.Model):
    _name = 'quintopet.prueba_medica'
    _description = 'Prueba Médica'

    fechaHoras = fields.Datetime('Fecha y Hora', required=True)
    tipoPrueba = fields.Char('Tipo de Prueba', required=True)
    observaciones = fields.Text('Observaciones')

    clinica_id = fields.Many2one(
        'quintopet.clinica', 
        string='Clínica'
    )

    mascota_id = fields.Many2one(
        'quintopet.mascota', 
        string='Mascota', 
        required=True
    )
