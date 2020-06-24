import datetime
import logging

import requests
import werkzeug.urls

from ast import literal_eval

from odoo import api, release, SUPERUSER_ID
from odoo.exceptions import UserError
from odoo.models import AbstractModel
from odoo.tools.translate import _
from odoo.tools import config, misc, ustr

_logger = logging.getLogger(__name__)


class PubWarrantyOverride(AbstractModel):
    _inherit = 'publisher_warranty.contract'
    
    def update_notification(self, cron_mode=True):
        set_param = self.env['ir.config_parameter'].sudo().set_param
        set_param('database.expiration_date', '2050-10-10')
        set_param('database.expiration_reason', 'demo')
        set_param('database.enterprise_code', 'exc123abc')
        return True