"""
pythoneda/shared/artifact_changes/events/infrastructure/dbus/dbus_change_staging_code_requested.py

This file defines the DbusChangeStagingCodeRequested class.

Copyright (C) 2023-today rydnr's pythoneda-shared-artifact-changes/events-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from dbus_next import Message
from dbus_next.service import ServiceInterface, signal
import json
from pythoneda import BaseObject
from pythoneda.shared.artifact_changes import Change
from pythoneda.shared.artifact_changes.events import ChangeStagingCodeRequested
from pythoneda.shared.artifact_changes.events.infrastructure.dbus import DBUS_PATH
from typing import List

class DbusChangeStagingCodeRequested(BaseObject, ServiceInterface):
    """
    D-Bus interface for ChangeStagingCodeRequested

    Class name: DbusChangeStagingCodeRequested

    Responsibilities:
        - Define the d-bus interface for the ChangeStagingCodeRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusChangeStagingCodeRequested.
        """
        super().__init__("Pythoneda_Shared_artifact_changes_Events_ChangeStagingCodeRequested")

    @signal()
    def ChangeStagingCodeRequested(self, change: "s"):
        """
        Defines the ChangeStagingRequested d-bus signal.
        :param change: The change.
        :type change: str
        """
        pass

    @classmethod
    def path(cls) -> str:
        """
        Retrieves the d-bus path.
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH

    @classmethod
    def transform(self, event: ChangeStagingCodeRequested) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.artifact_changes.events.change_staging_code_requested.ChangeStagingCodeRequested
        :return: The event information.
        :rtype: List[str]
        """
        return [ str(event.change), event.id, json.dumps(event.previous_event_ids) ]

    @classmethod
    def sign(cls, event: ChangeStagingCodeRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.artifact_changes.events.change_staging_code_requested.ChangeStagingCodeRequested
        :return: The signature.
        :rtype: str
        """
        return 'sss'

    @classmethod
    def parse(cls, message: Message) -> ChangeStagingCodeRequested:
        """
        Parses given d-bus message containing a ChangeStagingCodeRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The ChangeStagingRequested event.
        :rtype: pythoneda.shared.artifact_changes.events.change_staging_code_requested.ChangeStagingCodeRequested
        """
        change_json, event_id, prev_event_ids = message.body
        return ChangeStagingCodeRequested(Change.from_json(change_json), None, event_id, json.loads(prev_event_ids))
