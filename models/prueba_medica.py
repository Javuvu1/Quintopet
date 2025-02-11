from odoo import models, fields, api
from odoo.exceptions import UserError

class prueba_medica(models.Model):
    _name = 'quintopet.prueba_medica'
    _description = 'Prueba Médica'

    fechaHoras = fields.Datetime('Fecha y Hora', required=True)
    tipoPrueba = fields.Char('Tipo de Prueba', required=True)
    observaciones = fields.Text('Observaciones')

    state = fields.Selection([('cancelada','Prueba médica cancelada'),
                                ('enCurso','Prueba médica confirmada')], 'Estado', default='enCurso', required=True)

    clinica_id = fields.Many2one(
        'quintopet.clinica', 
        string='Clínica',
        required=True
    )

    mascota_id = fields.Many2one(
        'quintopet.mascota', 
        string='Mascota', 
        required=True
    )
    def btn_submit_to_enCurso(self):
        if not self.state:
            raise UserError("El campo 'state' está vacío o no válido.")
        if self.state == 'paga_siempre':
            raise UserError("La prueba medica ya está confirmada'.")
        self.write({'state': 'enCurso'})

    def btn_submit_to_cancelada(self):
        if self.state == 'cancelada':
            raise UserError("La prueba médica ya esta cancelada.")
        self.write({'state': 'cancelada'})
