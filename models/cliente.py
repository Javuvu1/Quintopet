# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class Cliente(models.Model):
    _inherit = "quintopet.persona"
    _name = 'quintopet.cliente' # modulo.modelo
    _description = 'Un cliente'
    
    direccion = fields.Char("Dirección", size=64, required=False)
    tipo = fields.Selection([
        ('particular', 'Particular'),
        ('fundacion', 'Fundación'),
        ('empresa_publica', 'Empresa Pública'),
        ('empresa_privada', 'Empresa Privada')
    ], "Tipo de cliente", default='particular', required=True)
    
    state = fields.Selection([('no_paga','Dudoso pago'),
                                ('paga_siempre','Paga Siempre')], 'Estado', default='paga_siempre', required=True)
    
    mascota_ids = fields.One2many(
        'quintopet.mascota',  # Nombre técnico del modelo relacionado
        'cliente_id',         # Nombre del campo Many2one en el modelo 'Mascota'
        string='Mascotas'
    )
    
    def btn_submit_to_pagasiempre(self):
        if not self.state:
            raise UserError("El campo 'state' está vacío o no válido.")
        if self.state == 'paga_siempre':
            raise UserError("El cliente ya está marcado como 'Paga Siempre'.")
        self.write({'state': 'paga_siempre'})

    def btn_submit_to_nopaga(self):
        if self.state == 'no_paga':
            raise UserError("El cliente ya está marcado como 'Dudoso pago'.")
        self.write({'state': 'no_paga'})
