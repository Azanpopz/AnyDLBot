#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import os


class Config(object):
   

    

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "")

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)


    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    CAPTION = os.environ.get("CAPTION", "@Mo_Tech_YT @Mo_Tech_Group")
    BUTTON_TEXT = os.environ.get("BUTTON", "🔻Join Channel🔻")
    URL_LINK = os.environ.get("LINK", "T.ME/MO_TECH_YT")
    USERNAME = os.environ.get("USERNAME", "")

    

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "")

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
