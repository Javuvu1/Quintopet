# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class Mascota(models.Model):
    _name = 'quintopet.mascota'
    _description = 'Una mascota'
    
    name = fields.Char("Nombre", size=64, required=True)
    sexo = fields.Selection([
        ('macho', 'Macho'), 
        ('hembra', 'Hembra')
        ], 'Sexo', required=True)
    numChip = fields.Integer("Número de chip", size=7, required=True)
    especie = fields.Char("Especie", size=64, required=True)
    edad = fields.Integer("Edad", size=2, required=True)
    color = fields.Char("Color", size=64, required=False)
    peso = fields.Float('Peso', size=3, required=True)
    raza = fields.Char('Raza', size=64, required=True)
    foto = fields.Binary('Foto', attachment=True)

    state = fields.Selection([('vacunado', 'Vacunado'),
                              ('por_vacunar', 'Por Vacunar')], 'Estado', default='por_vacunar', required=True)
    
    cliente_id = fields.Many2one(
        'quintopet.cliente', 
        string='Cliente',     
        required=False         
    )
    
    cita_ids = fields.One2many(
        'quintopet.cita',  
        'mascota_id',      
        string='Cita'     
    )

    prueba_medica_ids = fields.One2many(
        'quintopet.prueba_medica', 
        'mascota_id',              
        string='Pruebas Médicas'    
    )

    def btn_submit_to_vacunado(self):
        if not self.state:
            raise UserError("El campo 'state' está vacío o inválido.")
        if self.state == 'vacunado':
            raise UserError("La mascota ya está marcada como 'Vacunado'.")
        self.write({'state': 'vacunado'})

    def btn_submit_to_novacunado(self):
        if self.state == 'por_vacunar':
            raise UserError("La mascota ya está marcada como 'Por Vacunar'.")
        self.write({'state': 'por_vacunar'})

    @api.constrains('numChip')
    def _check_capacity(self):
        if self.numChip > 9999999: 
            raise ValidationError('El número de chip no puede ser mayor a 7 dígitos')
        
    @api.constrains('edad')
    def _check_edad(self):
        """Valida que la edad esté entre 0 y 30 años."""
        for mascota in self:
            if mascota.edad < 0 or mascota.edad > 30:
                raise ValidationError("La edad de la mascota debe estar entre 0 y 30 años.")
    