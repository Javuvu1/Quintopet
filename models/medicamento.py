# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
import re

class Medicamento(models.Model):
    _name = 'quintopet.medicamento'  
    _description = 'Un medicamento'
    
    nombreMedicamento = fields.Char("Nombre del Medicamento", size=64, required=True)
    referencia = fields.Char("Referencia", size=32, required=True)
    precio = fields.Float("Precio", required=True)  
    prospecto = fields.Binary("Prospecto")
    stock = fields.Selection([
        ('en_stock', 'En stock'),
        ('sin_stock', 'Sin stock'),
    ], 'Estado', default='en_stock', required=True)
    fechaCaducidad = fields.Date("Fecha de caducidad", default=fields.Date.context_today)

    tratamiento_ids = fields.Many2many(
        'quintopet.tratamiento',  
        'tratamiento_medicamento_rel', 
        'medicamento_id',  
        'tratamiento_id',  
        string='Tratamientos'  
    )

# Constraint: La referencia debe ser única
    @api.constrains('referencia')
    def _check_referencia_unique(self):
        for record in self:
            existing_meds = self.search([('referencia', '=', record.referencia), ('id', '!=', record.id)])
            if existing_meds:
                raise ValidationError("La referencia '{}' ya está registrada para otro medicamento.".format(record.referencia))
            
    # Onchange: Si el precio es mayor a 100, cambia automáticamente el stock a "En stock"
    @api.onchange('precio')
    def _onchange_precio(self):
        if self.precio > 100:
            self.stock = 'en_stock'

    def btn_submit_to_enstock(self):
        if self.stock == 'en_stock':
            raise UserError("El medicamento ya está marcado como 'En stock'.")
        self.write({'stock': 'en_stock'})

    def btn_submit_to_sinstock(self):
        if self.stock == 'sin_stock':
            raise UserError("El medicamento ya está marcado como 'Sin stock'.")
        self.write({'stock': 'sin_stock'})
        
    @api.constrains('referencia')
    def _check_referencia_format(self):
        ref_pattern = r'^[A-Z]{2}\d{4}$'  # 2 letras mayúsculas seguidas de 4 números
        for record in self:
            if not re.match(ref_pattern, record.referencia):
                raise ValidationError("La referencia '{}' no tiene un formato válido. Debe ser 2 letras mayúsculas seguidas de 4 números (Ejemplo: AB1234).".format(record.referencia))