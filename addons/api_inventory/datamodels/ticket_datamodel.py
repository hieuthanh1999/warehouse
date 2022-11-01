from marshmallow import fields
from odoo.addons.datamodel.core import Datamodel


class ticket_input(Datamodel):
    _name = "ticket.input"

    subject = fields.String(required=True)
    description = fields.String(required=True)