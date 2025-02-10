# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import re


class Cliente(models.Model):
    _inherit = "quintopet.persona"
    _name = 'quintopet.cliente'  # modulo.modelo
    _description = 'Un cliente'
    
    direccion = fields.Char("Dirección", size=64, required=False)
    tipo = fields.Selection([
        ('particular', 'Particular'),
        ('fundacion', 'Fundación'),
        ('empresa_publica', 'Empresa Pública'),
        ('empresa_privada', 'Empresa Privada')
    ], "Tipo de cliente", default='particular', required=True)

    state = fields.Selection([
        ('no_paga', 'Dudoso pago'),
        ('paga_siempre', 'Paga Siempre')
    ], 'Estado', default='paga_siempre', required=True)

    mascota_ids = fields.One2many(
        'quintopet.mascota',  # Nombre técnico del modelo relacionado
        'cliente_id',  # Nombre del campo Many2one en el modelo 'Mascota'
        string='Mascotas'
    )

    total_mascotas = fields.Integer(
        string="Número de Mascotas", compute="_compute_total_mascotas", store=True
    )

    dni = fields.Char("DNI", required=True)

    # Constraint: El DNI debe ser único
    @api.constrains('dni')
    def _check_dni_unique(self):
        for record in self:
            existing_clients = self.search([('dni', '=', record.dni), ('id', '!=', record.id)])
            if existing_clients:
                raise ValidationError("El DNI '{}' ya está registrado para otro cliente.".format(record.dni))
            

    # Onchange: Si el cliente es una fundación, cambia automáticamente el estado a "Paga Siempre"
    @api.onchange('tipo')
    def _onchange_tipo(self):
        if self.tipo == 'fundacion':
            self.state = 'paga_siempre'

    def btn_submit_to_pagasiempre(self):
        if self.state == 'paga_siempre':
            raise UserError("El cliente ya está marcado como 'Paga Siempre'.")
        self.write({'state': 'paga_siempre'})

    def btn_submit_to_nopaga(self):
        if self.state == 'no_paga':
            raise UserError("El cliente ya está marcado como 'Dudoso pago'.")
        self.write({'state': 'no_paga'})
        
        import re

    @api.constrains('dni')
    def _check_dni_format(self):
        dni_pattern = r'^\d{8}[A-Z]$'  # 8 números seguidos de una letra mayúscula
        for record in self:
            if not re.match(dni_pattern, record.dni):
                raise ValidationError("El DNI '{}' no tiene un formato válido. Debe ser 8 números seguidos de una letra (Ejemplo: 12345678A).".format(record.dni))
    
    @api.constrains('email')
    def _check_email_unique(self):
        for record in self:
            if record.email:
                existing_clients = self.search([('email', '=', record.email), ('id', '!=', record.id)])
                if existing_clients:
                    raise ValidationError("El email '{}' ya está registrado para otro cliente.".format(record.email))


        
        
