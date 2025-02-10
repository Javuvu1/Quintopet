from odoo import models, fields, api

class PruebaMedica(models.Model):
    _name = 'quintopet.pruebamedica'
    _description = 'Prueba Médica'

    fechaHora = fields.Datetime('Fecha y Hora', required=True)
    tipoPrueba = fields.Char('Tipo de Prueba', required=True)
    observaciones = fields.Text('Observaciones')

    clinica_id = fields.Many2one(
        'quintopet.clinica', 
        string='Clínica'
    )

    mascota_id = fields.Many2one(
        'quintopet.mascota',  # Relación con Mascota
        string='Mascota', 
        required=True
    )
