import os
import logging

from django.utils.translation import ugettext as _
from django.utils.encoding import smart_str

from ...models import Language
from ..base import GeoBaseCommand

from ...utils.common import *
from ...utils.downloader import *
from ...utils.handler import *

logger = logging.getLogger("geoware.cmd.language")


class Command(GeoBaseCommand):
    cmd_name = "language"
